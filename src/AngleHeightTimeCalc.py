import math

import sys
sys.path.append('src/')
import config

def AngleHeightTimeCalc(angle, init_height, time):
    #non zero checks
    if angle == 0 or time == 0:
        return [0, 0, 0]

    #finding the velocity
    speed_vertical = (-1 * init_height + (config.G_CONSTANT * time ** 2) / 2 - 0) / time
    speed = speed_vertical / math.sin(math.radians(angle))

    #finding the distance
    speed_horizontal = speed * math.cos(math.radians(angle))
    distance = speed_horizontal * time

    #finding maximum height
    max_height = init_height + speed_vertical ** 2 / (2 * config.G_CONSTANT)

    return [distance, speed, max_height]
