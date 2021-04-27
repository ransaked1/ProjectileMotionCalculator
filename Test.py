from termcolor import colored

import sys
sys.path.append('../')

from src.AngleHeightTimeCalc import AngleHeightTimeCalc
from src.HeightTimeDistanceCalc import HeightTimeDistanceCalc
from src.VelocityHeightAngleCalc import VelocityHeightAngleCalc
from src.HeightTimeCalc import HeightTimeCalc

while 1:
    print("This program calculates the unknown varaiables in a projectiles motion problem given some input variables.\n\nCurrently availabe input options are:\n1. Angle, height and time\n2. Height, time, distance\n3. Velocity, height, angle\n4. Height, time\n")

    choice = input("Type the number of the option you are interested in or 0 to exit: ")
    try:
        choice = float(choice)
    except:
        print(colored("Invalid input!", 'red'))
        pass

    if choice == 0:
        break
    elif choice == 1:
        try:
            angle = float(input("What is the angle the projectile is launched at (degrees)?\n"))
            height = float(input("What is the initial height the projectile is launched at (meters)?\n"))
            time = float(input("What is the time the projectile travels (seconds)?\n"))

            result = AngleHeightTimeCalc(angle, height, time)
            print(colored("\nDistance traveled:", 'green'), int(result[0]), "m")
            print(colored("Speed:", 'green'), int(result[1]), "m/s")
            print(colored("Maximum height of projectile:", 'green'), int(result[2]), "m\n")
            input()
        except Exception as error:
            print(colored("\nThere was an issue with your input, try again.\n", 'red'), colored(str(error) + "\n\n", 'red'))
    elif choice == 2:
        try:
            height = float(input("What is the initial height the projectile is launched at (meters)?\n"))
            time = float(input("What is the time the projectile travels (seconds)?\n"))
            distance = float(input("What is the distance the projectile travels (meters)\n"))

            result = HeightTimeDistanceCalc(height, time, distance)
            print(colored("\nAngle of projectile launch:", 'green'), int(result[0]), "degrees")
            print(colored("Speed:", 'green'), int(result[1]), "m/s")
            print(colored("Maximum height of projectile:", 'green'), int(result[2]), "m\n")
            input()
        except Exception as error:
            print(colored("\nThere was an issue with your input, try again.\n", 'red'), colored(str(error) + "\n\n", 'red'))
    elif choice == 3:
        try:
            speed = float(input("What is the initial velocity of the projectile is launched at (m/s)?\n"))
            height = float(input("What is the initial height the projectile is launched at (meters)?\n"))
            angle = float(input("What is the angle the projectile is launched at (degrees)?\n"))

            result = VelocityHeightAngleCalc(speed, height, angle)
            print(colored("\nDistance traveled:", 'green'), int(result[0]), "m")
            print(colored("Time the projectile travels:", 'green'), int(result[1]), "sec")
            print(colored("Maximum height of projectile:", 'green'), int(result[2]), "m\n")
            input()
        except Exception as error:
            print(colored("\nThere was an issue with your input, try again.\n", 'red'), colored(str(error) + "\n\n", 'red'))
    elif choice == 4:
        try:
            height = float(input("What is the initial height the projectile is launched at (meters)?\n"))
            time = float(input("What is the time the projectile travels (seconds)?\n"))

            result = HeightTimeCalc(height, time)
            print(colored("\nMaximum height of projectile:", 'green'), int(result), "m\n")
            input()
        except Exception as error:
            print(colored("\nThere was an issue with your input, try again.\n", 'red'), colored(str(error) + "\n\n", 'red'))
    else:
        print(colored("There is no such option available. Input a valid option between 0 and 4\n\n", 'red'))
