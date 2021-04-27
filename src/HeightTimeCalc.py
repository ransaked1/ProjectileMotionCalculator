import math

import sys
sys.path.append('src/')
import config

def HeightTimeCalc(init_height, time):
    #non zero checks
    if time == 0:
        return 0

    #finding the maximum height
    speed_vertical = (config.G_CONSTANT * time ** 2 / 2 - init_height) / time
    max_height = init_height + speed_vertical ** 2 / (2 * config.G_CONSTANT)

    return max_height
