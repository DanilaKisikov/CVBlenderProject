import image_location
import location

video_path = "video.mp4"


class Object:
    def __init__(self, name, figure, color, reference_path, real_size, locations=None):
        self.name = figure
        self.figure = figure
        self.color = color
        self.reference_path = reference_path
        self.real_size = real_size

        self.locations = locations

    def calc_object_locations(self):
        image_locations = image_location.get_image_locations(self.reference_path)

        self.locations = location.get_locations(image_locations, self.real_size)
