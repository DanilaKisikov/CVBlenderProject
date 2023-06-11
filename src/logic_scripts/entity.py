import src.logic_scripts.image_location as image_location
import src.logic_scripts.location as location
from pathlib import Path
import json


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

    def to_json(self):
        dictionary = {}

        name = self.name
        figure_type = self.figure
        color = self.color
        real_size = self.real_size

        coordinates = []

        for loc in self.locations:
            x = loc.x
            y = loc.y
            z = loc.z
            number = loc.num_0f_frame

            coordinates.append((x, y, z, number))

        dictionary["name"] = name
        dictionary["figure"] = figure_type.value
        dictionary["color"] = color.value
        dictionary["real_size"] = real_size
        dictionary["locations"] = coordinates

        file_name = name + ".json"
        path = Path(__file__).parent.absolute()
        save_path = path.parent.parent / "blender" / "saves" / file_name

        with open(save_path, "w") as file:
            json.dump(dictionary, file)

