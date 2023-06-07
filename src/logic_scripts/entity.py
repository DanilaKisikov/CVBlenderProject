import src.logic_scripts.image_location as image_location
import src.logic_scripts.location as location


class Entity:
    def __init__(self, name, figure, color, reference_path, real_size, locations=None, image_locations=None):
        self.name = name
        self.figure = figure
        self.color = color
        self.reference_path = reference_path
        self.real_size = real_size

        self.locations = locations
        self.image_locations = image_location

    def calc_entity_locations(self):
        self.image_locations = image_location.get_image_locations(self.reference_path)

        self.locations = location.get_locations(self.image_locations, self.real_size)
