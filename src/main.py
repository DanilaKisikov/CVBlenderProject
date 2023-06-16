import src.logic_scripts.entity as entity
from src import enums, video_shower

from src.logic_scripts import location
from src.logic_scripts import image_location
import src.video_shower
import src.enums as enum
from pathlib import Path


def main_function(marker, video, real_size, color, figure, name, angle, resize=None, ref_image=None, ref_dist=None,
                  focal_length=None):
    this_entity = entity.Entity(name=name, figure=figure, color=color, reference_path=marker, real_size=real_size)
    image_location.video_path = video
    location.angle = angle

    if focal_length is not None:
        location.focal_length = focal_length

    if ref_image is not None and ref_dist is not None:
        location.focal_length_finder(marker, ref_image, ref_dist, real_size)

    if resize is not None:
        image_location.resize_video[0] = resize[0]
        image_location.resize_video[1] = resize[1]
    else:
        image_location.resize_video = image_location.frame_size

    this_entity.calc_entity_locations()

    this_entity.to_json()

    while True:
        video_shower.show_with_rect(this_entity.locations, this_entity.image_locations, 60)


if __name__ == '__main__':
    videos_path = Path("D:\CVBlenderProject")
    marker = str(videos_path / "ref_sky.jpg")
    video = str(videos_path / "5 (2).mp4")

    ref_img = "photo_2023-06-07_18-13-48.jpg"
    print(marker)
    print(video)

    main_function(marker, video, 0.07, enums.Color.RED, enums.Figure.CUBE, "hello", 80)

    #  location.focal_length_finder(marker, ref_img, 0.2, 0.035)
