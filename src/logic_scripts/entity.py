import image_location
import location

video_path = "video.mp4"
frame_size = (0, 0)  # (w, h)


class Entity:
    def __init__(self, name, figure, color, reference_path, real_size, locations=None):
        self.name = name
        self.figure = figure
        self.color = color
        self.reference_path = reference_path
        self.real_size = real_size

        self.locations = locations

    def calc_entity_locations(self):
        image_locations = image_location.get_image_locations(self.reference_path)

        self.locations = location.get_locations(image_locations, self.real_size)
