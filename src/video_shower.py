import time

import cv2
import math
import src.logic_scripts.image_location as image_location
import src.logic_scripts.location

keep_loop = True


def show_with_rect(locations, image_locations, fps):
    global keep_loop
    video = cv2.VideoCapture(image_location.video_path)

    try:
        xK = image_location.frame_size[0] / image_location.resize_video[0]
        yK = image_location.frame_size[1] / image_location.resize_video[1]
    except:
        print("No resize")
        xK = 1
        yK = 1

    for i in range(len(locations)):
        img_x = math.floor(image_locations[i].get_x() * xK)
        img_y = math.floor(image_locations[i].get_y() * yK)
        wight = math.floor(image_locations[i].get_size() * xK)

        x = locations[i].get_x()
        y = locations[i].get_y()
        z = locations[i].get_z()

        distance = (x**2 + y**2 + z**2)**0.5

        text = "x: " + str(round(x, 3)) + " y: " + str(round(y, 3)) + " z: " + str(round(z, 3)) + " dist: " + \
               str(round(distance, 3))

        for a in range(image_location.section):
            ret, frame = video.read()

            if not ret:
                keep_loop = False
                break

            cv2.rectangle(frame, (img_x - math.floor(wight/2), img_y - 20), (img_x + math.floor(wight/2), img_y + 20)
                          , (0, 0, 255), 2)
            cv2.putText(frame, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                keep_loop = False
                break

            time.sleep(1/fps)

        if not keep_loop:
            break
