
# Validator expected input: velocity, angle, distance, time, init_height, max_height, gravity
def InputValidator(*args):
    velocity = args[0]
    angle = args[1]
    distance = args[2]
    time = args[3]
    init_height = args[4]
    max_height = args[5]
    gravity = args[6]

    if velocity < 0:
        return 0
    elif angle < 0 or angle > 90:
        return 1
    elif distance < 0:
        return 2
    elif time < 0:
        return 3
    elif init_height < 0:
        return 4
    elif max_height < 0:
        return 5
    elif gravity <= 0:
        return 6
    else:
        return -1
