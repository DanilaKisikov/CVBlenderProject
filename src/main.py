import src.logic_scripts.entity as entity
import video_shower
from src.logic_scripts import location
from src.logic_scripts import image_location
import src.video_shower
import enums


def main_function(marker, video, real_size, color, figure, name, angle, resize=None, ref_image=None, ref_dist=None):
    this_entity = entity.Entity(name=name, figure=figure, color=color, reference_path=marker, real_size=real_size)
    image_location.video_path = video
    location.angle = angle

    if ref_image is not None and ref_dist is not None:
        location.focal_length_finder(marker, ref_image, ref_dist, real_size)

    if resize is not None:
        image_location.resize_video = resize
    else:
        image_location.resize_video = image_location.frame_size

    this_entity.calc_entity_locations()

    while True:
        video_shower.show_with_rect(this_entity.locations, this_entity.image_locations, 30)

    # блендер скрипт


if __name__ == '__main__':
    marker = "ref-point.jpg"
    video = "video.mp4"
    print(marker)
    print(video + '\n')

    main_function(marker, video, 0.06, enums.Color.RED, enums.Figure.CUBE, "hello", 110, resize=[480, 640])
