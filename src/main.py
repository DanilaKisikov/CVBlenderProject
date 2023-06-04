import logic_scripts.entity as entity
from src.logic_scripts import location


def main_function(marker, video, real_size, color, figure, name, angle, ref_image=None, ref_dist=None):
    this_entity = entity.Entity(name=name, figure=figure, color=color, reference_path=marker, real_size=real_size)
    entity.video_path = video
    location.angle = angle

    if ref_image is not None and ref_dist is not None:
        location.focal_length_finder(marker, ref_image, ref_dist, real_size)

    this_entity.calc_entity_locations()

    # блендер скрипт
