import math

def calculationFunctionVelocityY(initVelocity, time, g_value, angle):
    initVelocityY = initVelocity * math.sin(math.radians(angle))

    velocityY = initVelocityY - g_value * time

    if velocityY < 0.1 and velocityY > 0:
        velocityY = 0

    return velocityY

def GraphDataGeneratorVelocityY(time, initVelocity, stepCount, g_value, angle):
    stepSizeX = time / stepCount
    valueListX = []
    valueListY = []

    for i in range(stepCount):
        valueListX.append(i * stepSizeX)
    valueListX.append(time)

    for i in range(stepCount + 1):
        valueListY.append(calculationFunctionVelocityY(initVelocity, valueListX[i], g_value, angle))

    return valueListX, valueListY
