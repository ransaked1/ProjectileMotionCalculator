import math

import sys
sys.path.append('src/')
import config

def HeightTimeDistanceCalc(init_height, time, distance):
    #non zero checks
    if time == 0 or distance == 0:
        return [0, 0, 0]

    #finding the velocity
    speed_horizontal = distance / float(time)
    speed_vertical = (config.G_CONSTANT * distance) / (2 * speed_horizontal)
    speed = math.sqrt(speed_horizontal ** 2 + speed_vertical**2)

    #finding the angle
    angle = math.degrees(math.acos(speed_horizontal / speed))

    #finding the maximum height
    max_height = init_height + speed_vertical ** 2 / (2 * config.G_CONSTANT)

    return [speed, angle, max_height]
