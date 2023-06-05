import math

import image_location
from entity import frame_size

focal_length = 35  # mm
angleInDegrees = 110
angle = angleInDegrees * math.pi / 180


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


def get_locations(image_locations, real_size):
    locations = []

    for loc in image_locations:
        location = calc_location(loc, real_size)
        locations.append(location)

    return locations


def calc_location(image_loc, real_size):
    num_of_frame = image_loc.get_num_of_frame()

    image_x = image_loc.get_x()
    image_y = image_loc.get_y()
    on_image_size = image_loc.get_size()

    distance = (real_size * focal_length) / on_image_size

    xAngle = 2 * angle * (image_x - frame_size[0]/2) / frame_size[0]
    yAngle = 2 * angle * (image_y - frame_size[1]/2) / frame_size[0]

    tanX = math.tan(xAngle)
    tanY = math.tan(yAngle)

    cosY = 1 / (tanX**2 + tanY**2 + 1)**0.5

    z = distance * cosY

    x = z * tanX

    y = z * tanY

    location = Location(x, y, z, image_loc.get_num_of_frame)

    return location


def focal_length_finder(reference_path, ref_image, ref_distance, real_size):
    reference = cv2.imread(reference_path)
    x, y, on_image_size = image_location.detect(ref_image, reference)

    global focal_length
    focal_length = (on_image_size * ref_distance) / real_size
