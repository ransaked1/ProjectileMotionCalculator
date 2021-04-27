import math

def calculationFunctionVelocity(initVelocity, time, g_value, angle):
    initVelocityX = initVelocity * math.cos(math.radians(angle))
    initVelocityY = initVelocity * math.sin(math.radians(angle))

    velocityX = initVelocityX
    velocityY = initVelocityY - g_value * time

    velocity = math.sqrt(velocityX ** 2 + velocityY ** 2)

    return velocity

def GraphDataGeneratorVelocity(time, initVelocity, stepCount, g_value, angle):
    stepSizeX = time / stepCount
    valueListX = []
    valueListY = []

    for i in range(stepCount):
        valueListX.append(i * stepSizeX)
    valueListX.append(time)

    for i in range(stepCount + 1):
        valueListY.append(calculationFunctionVelocity(initVelocity, valueListX[i], g_value, angle))

    return valueListX, valueListY
