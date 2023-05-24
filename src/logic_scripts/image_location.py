import numpy as np
from entity import video_path
import cv2

section = 10


class ImageLocation:
    def __init__(self, x, y, size, num_of_frame):
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
    video = cv2.VideoCapture(video_path)
    reference = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

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
            if not ret:
                keep_loop = False
                break

            number += 1

            x, y, size = detect(frame, reference)

            xes[i] = x
            yes[i] = y
            sizes[i] = size

        image_loc = ImageLocation(np.median(xes), np.median(yes), np.median(sizes), this_number)

        image_locations.append(image_loc)

    return image_locations


def detect(frame, reference):
    x = None
    y = None
    size = None

    # Тут нужно сделать супер детектор

    return x, y, size
