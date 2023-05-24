class Location:
    def __init__(self, x, y, z, num_of_frame):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


def get_locations(image_locations, angle):
    locations = []

    for loc in image_locations:
        num_of_frame = loc.get_num_of_frame

        location = calc_location(loc)

        locations.append(location)

    return locations


def calc_location(image_location):

    # Супер тригонометрия

    location = Location()

    return location
