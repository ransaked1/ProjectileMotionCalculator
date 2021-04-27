import math

def calculationFunctionHeight(initHeight, time, g_value, angle, initVelocity):
    initVelocityY = initVelocity * math.sin(math.radians(angle))

    velocityY = initVelocityY - g_value * time

    height = initHeight + initVelocityY * time - 0.5 * g_value * time ** 2

    return height

def GraphDataGeneratorHeight(time, initHeight, stepCount, g_value, angle, initVelocity):
    stepSizeX = time / stepCount
    valueListX = []
    valueListY = []

    for i in range(stepCount):
        valueListX.append(i * stepSizeX)
    valueListX.append(time)

    for i in range(stepCount):
        valueListY.append(calculationFunctionHeight(initHeight, valueListX[i], g_value, angle, initVelocity))
    valueListY.append(0)

    return valueListX, valueListY
