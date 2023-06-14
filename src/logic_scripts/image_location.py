import time
from pathlib import Path

import numpy as np
import cv2

from src.logic_scripts import entity

section = 10
video_path = "video.mp4"
frame_size = [0, 0]  # (w, h)
resize_video = [0, 0]
MIN_MATCH_COUNT = 3
reference_resize_px = 96

previous = None
sift = None
desMarker = None
flann = None


class ImageLocation:
    def __init__(self, x, y, size, num_of_frame=None):
        self.x = x
        self.y = y
        self.size = size
        self.num_of_frame = num_of_frame

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size

    def get_num_of_frame(self):
        return self.num_of_frame


def get_image_locations(reference_path):
    start_time = time.perf_counter()
    print("video " + video_path)
    print("image " + reference_path)
    video = cv2.VideoCapture(video_path)

    reference = cv2.imread(reference_path)
    # assert not isinstance(reference, type(None)), 'image not found'
    reference_h, reference_w = reference.shape[:2]
    reference_max = max(reference_h, reference_w)
    reference_k = reference_resize_px/reference_max
    reference = cv2.resize(reference, (int(reference_h*reference_k), int(reference_w*reference_k)),
                           interpolation=cv2.INTER_LINEAR)

    init_sift(reference)

    keep_loop = True
    number = 0

    image_locations = []

    while keep_loop:
        xes = np.eye(section, 1)
        yes = np.eye(section, 1)
        sizes = np.eye(section, 1)

        this_number = number
        for i in range(section):
            ret, frame = video.read()

            if number == 0:
                height, width = frame.shape[:2]
                frame_size[0] = width
                frame_size[1] = height
                print("frame size " + str(frame_size))
                print("resize video " + str(resize_video))

            if not ret:
                keep_loop = False
                break

            if resize_video[0] != 0:
                try:
                    frame = cv2.resize(frame, resize_video, interpolation=cv2.INTER_LINEAR)
                except:
                    print("wtf?")

            number += 1

            # loc = detect(frame, reference)
            loc = detect2(frame)

            xes[i] = loc.get_x()
            yes[i] = loc.get_y()
            sizes[i] = loc.get_size()

        image_loc = ImageLocation(np.median(xes), np.median(yes), np.median(sizes), this_number)

        image_locations.append(image_loc)
        print("x: " + str(image_loc.get_x()) + " y: " + str(image_loc.get_y()) + " size: " + str(image_loc.get_size()))
        print('got ' + str(number) + ' frames. It took ' + str(round(time.perf_counter() - start_time, 2)) + '\n')

    return image_locations


def detect(frame, reference):

    template = cv2.cvtColor(reference, cv2.IMREAD_GRAYSCALE)
    frame_gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)

    w, h, c = template.shape[::-1]

    result = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)

    threshold = np.mean(result) + 2 * np.std(result)

    loc = np.where(result >= threshold)

    rectangles = []
    for pt in zip(*loc[::-1]):
        rectangles.append([pt[0], pt[1], pt[0] + w, pt[1] + h])

    rectangles = non_max_suppression(np.array(rectangles), 0.3)

    locations = []

    for rect in rectangles:
        x = (rect[0] + rect[2])/2
        y = (rect[1] + rect[3])/2
        size = rect[2] - rect[0]
        location = ImageLocation(x=x, y=y, size=size)

        locations.append(location)

    image_location = choose_location(locations)

    return image_location


def non_max_suppression(boxes, overlapThresh):
    if len(boxes) == 0:
        return []

    pick = []
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    ids = np.argsort(y2)

    while len(ids) > 0:
        last = len(ids) - 1
        i = ids[last]
        pick.append(i)
        suppress = [last]

        for pos in range(0, last):
            j = ids[pos]
            xx1 = max(x1[i], x1[j])
            yy1 = max(y1[i], y1[j])
            xx2 = min(x2[i], x2[j])
            yy2 = min(y2[i], y2[j])

            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)

            overlap = float(w * h) / area[j]

            if overlap > overlapThresh:
                suppress.append(pos)

        ids = np.delete(ids, suppress)

    return boxes[pick]


def choose_location(locations):
    global previous
    if len(locations) == 0:
        return ImageLocation(None, None, None, None)
    if previous is None:
        previous = locations[0]
        return locations[0]
    if len(locations) == 1:
        previous = locations[0]
        return locations[0]

    result = locations[0]
    result_dist = ((result.get_x() - previous.get_x())**2 + (result.get_x() - previous.get_x())**2)**0.5

    for i in range(1, len(locations)):
        this_dist = ((locations[i].get_x() - previous.get_x())**2 + (locations[i].get_x() - previous.get_x())**2)**0.5
        if this_dist < result_dist:
            result = locations[i]
            result_dist = this_dist

    previous = result
    return result


def init_sift(marker):
    global sift
    global desMarker
    global flann
    sift = cv2.SIFT_create()
    kpMarker, desMarker = sift.detectAndCompute(marker, None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=50)
    search_params = dict(checks=100)
    flann = cv2.FlannBasedMatcher(index_params, search_params)


def detect2(frame):
    global previous
    kp, des = sift.detectAndCompute(frame, None)

    matches = flann.knnMatch(des, desMarker, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp[m.queryIdx].pt for m in good])
        x = round(np.average(src_pts[:, 0]))
        y = round(np.average(src_pts[:, 1]))

        size = np.max(src_pts[:, 0]) - np.min(src_pts[:, 0])

        location = ImageLocation(x=x, y=y, size=size)
        previous = location
        return location
    else:
        if previous is None:
            return ImageLocation(None, None, None, None)
        else:
            return previous
