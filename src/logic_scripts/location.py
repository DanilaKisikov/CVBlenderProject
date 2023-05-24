import image_location

angle = 110


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
    onimage_size = image_loc.get_size()

    # Супер тригонометрия

    location = Location()

    return location
