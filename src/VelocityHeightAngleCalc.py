import math

import sys
sys.path.append('src/')
import config

def VelocityHeightAngleCalc(speed, init_height, angle):
    #non zero checks
    if speed == 0:
        return [0, 0, 0]

    #finding maximum height
    speed_vertical = speed * math.sin(math.radians(angle))
    max_height = init_height + speed_vertical ** 2 / (2 * config.G_CONSTANT)

    #finding the time
    time = (speed_vertical + math.sqrt(speed_vertical ** 2 + 2 * config.G_CONSTANT *init_height)) / config.G_CONSTANT

    #finding the distance
    speed_horizontal = speed * math.cos(math.radians(angle))
    distance = speed_horizontal * time

    return [distance, time, max_height]
