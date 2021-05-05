
# Validator expected input: velocity, angle, distance, time, init_height, max_height, gravity
def InputValidator(*args):
    velocity = args[0]
    angle = args[1]
    distance = args[2]
    time = args[3]
    init_height = args[4]
    max_height = args[5]
    gravity = args[6]

    resultArray = [0,0,0,0,0,0,0]

    if velocity < 0:
        resultArray[0] = 1
    if angle < 0 or angle > 90:
        resultArray[1] = 1
    if distance < 0:
        resultArray[2] = 1
    if time < 0:
        resultArray[3] = 1
    if init_height < 0:
        resultArray[4] = 1
    if max_height < 0:
        resultArray[5] = 1
    if gravity <= 0:
        resultArray[6] = 1

    return resultArray
