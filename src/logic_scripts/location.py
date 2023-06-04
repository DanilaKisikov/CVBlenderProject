import image_location

focal_length = 35  # mm
angle = 110  # degrees


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

    #  тут нужно сделать расчёт координат

    location = Location()

    return location


def focal_length_finder(reference_path, ref_image, ref_distance, real_size):
    reference = cv2.imread(reference_path)
    x, y, on_image_size = image_location.detect(ref_image, reference)

    global focal_length
    focal_length = (on_image_size * ref_distance) / real_size
