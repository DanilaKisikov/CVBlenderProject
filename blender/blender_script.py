import json
import bpy
from mathutils import Vector
from pathlib import Path


# enter file name
fileName = "hello.json"

path = Path(__file__).parent.absolute().parent / fileName

obj = None

dictionary = None


def anim(locations):
    global obj
    for loc in locations:
        x = loc[0]
        y = loc[1]
        z = loc[2]
        number = loc[3]

        obj.location = [x, y, z]
        obj.keyframe_insert(data_path="location", frame=number * 2)


def create_figure():
    global obj
    name = dictionary["name"]
    figure = dictionary["figure"]
    color = dictionary["color"]
    real_size = dictionary["real_size"]

    bpyscene = bpy.context.scene
    if figure == "Cube":
        bpy.ops.mesh.primitive_cube_add(size=real_size, location=(0, 0, 0), rotation=(0, 0, 0))
        obj = bpy.context.object
    else:
        bpy.ops.mesh.primitive_uv_sphere_add(size=real_size, location=(0, 0, 0), rotation=(0, 0, 0))
        obj = bpy.context.object

    obj.name = name


def from_json():
    global dictionary
    with open(path, "r") as file:
        dictionary = json.load(file)


if __name__ == '__main__':
    from_json()
    create_figure()
    anim(dictionary["locations"])
