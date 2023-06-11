import math
import cv2

import src.logic_scripts.image_location as image_location
from src.logic_scripts.image_location import frame_size, resize_video

focal_length = 23  # mm
angleInDegrees = 110
angle = angleInDegrees * math.pi / 180

previous = None


class Location:
    def __init__(self, x, y, z, num_of_frame):
        self.x = x
        self.y = y
        self.z = z
        self.num_0f_frame = num_of_frame

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_number_of_frame(self):
        return self.num_0f_frame

    def set_number_of_frame(self, n):
        self.num_0f_frame = n


def get_locations(image_locations, real_size):
    print("focal " + str(focal_length))
    print("angle " + str(angle))
    locations = []

    for loc in image_locations:
        location = calc_location(loc, real_size)
        locations.append(location)

        print("x: " + str(location.get_x()) + " y: " + str(location.get_y()) + " z: " + str(location.get_z()) + " frame: "
              + str(location.get_number_of_frame()))

    for loc in locations:
        print("(" + str(loc.x) + ", " + str(loc.y) + ", " + str(loc.z) + ", " + str(loc.get_number_of_frame()) + "), ")

    return locations


def calc_location(image_loc, real_size):
    global previous
    num_of_frame = image_loc.get_num_of_frame()

    image_x = image_loc.get_x()
    image_y = image_loc.get_y()
    on_image_size = image_loc.get_size()

    if on_image_size == 0:
        if previous is None:
            return Location(0, 0, 0, num_of_frame)
        else:
            previous.set_number_of_frame(num_of_frame)
            return previous

    distance = (real_size * focal_length) / on_image_size

    if resize_video[0] == 0:
        frame_x = frame_size[0]
        frame_y = frame_size[1]
    else:
        frame_x = resize_video[0]
        frame_y = resize_video[1]

    frame_s = max(frame_x, frame_y)

    deltaX = image_x - frame_x / 2
    deltaY = image_y - frame_y / 2

    L = 0.5 * frame_s / math.tan(angle / 2)

    tanX = deltaX / L
    tanY = deltaY / L

    cosY = 1 / (tanX**2 + tanY**2 + 1)**0.5

    z = distance * cosY

    x = z * tanX

    y = z * tanY

    location = Location(x, y, z, num_of_frame)

    previous = location

    return location


def focal_length_finder(reference_path, ref_image, ref_distance, real_size):
    reference = cv2.imread(reference_path)
    reference = cv2.resize(reference, (96, 64), interpolation=cv2.INTER_LINEAR)
    ref_image = cv2.imread(ref_image)
    loc = image_location.detect(ref_image, reference)

    global focal_length
    focal_length = (loc.size * ref_distance) / real_size

    print(focal_length)
