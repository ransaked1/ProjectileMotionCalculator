import tkinter as tk
import pygubu
import math

import sys
sys.path.append('src/')
import config

from AngleHeightTimeCalc import AngleHeightTimeCalc
from HeightTimeDistanceCalc import HeightTimeDistanceCalc
from VelocityHeightAngleCalc import VelocityHeightAngleCalc
from HeightTimeCalc import HeightTimeCalc
from GraphDataGeneratorVelocity import GraphDataGeneratorVelocity
from GraphDataGeneratorVelocityY import GraphDataGeneratorVelocityY
from GraphDataGeneratorHeight import GraphDataGeneratorHeight

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

initVelocity = 0.0;
launchAngle = 0.0;
distanceTraveled = 0.0;
flightTime = 0.0;
initHeight = 0.0;
maxHeight = 0.0;
initG = 9.81;

# Constants used for drawing properly
PADDING_X = 40
DRAW_AREA_Y = 450
DRAW_AREA_X = 775

# TO DO
# 1. Global gravity DONE
# 2. Graphs DONE
# 3. Draw trajectory DONE
# Reset input button! DONE
# 4. Input values and result validation
# 4. Values and vectors of projectile
# 5. Animation with slider and values changing
# 6. Theory buttons
# 7. Air resistance

class MainGraphics(tk.Frame):

    # Tkinter input field objects initialization
    inputVelocity = None;
    inputAngle = None;
    inputDistance = None;
    inputTime = None;
    inputInitHeight = None;
    inputMaxHeight = None;
    inputG = None;
    canvas = None

    passed = False;

    def __init__(self, master):
        super(MainGraphics, self).__init__()

        self.master = master

        # Create a builder
        self.builder = builder = pygubu.Builder()

        # Load an ui file
        builder.add_from_file('graphics/mainapp.ui')

        # Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow', master)

        # Linking input fields to variables
        self.inputVelocity = self.builder.get_object('input_vel')
        self.inputAngle = self.builder.get_object('input_angl')
        self.inputDistance = self.builder.get_object('input_dist')
        self.inputTime = self.builder.get_object('input_time')
        self.inputInitHeight = self.builder.get_object('input_init_h')
        self.inputMaxHeight = self.builder.get_object('input_max_h')
        self.inputG = self.builder.get_object('input_g')

        # Variable input fields triggers when value is changed
        self.builder.tkvariables['initVelocity'].trace("w", self.on_entry_vel)
        self.builder.tkvariables['launchAngle'].trace("w", self.on_entry_angl)
        self.builder.tkvariables['distanceTraveled'].trace("w", self.on_entry_dist)
        self.builder.tkvariables['flightTime'].trace("w", self.on_entry_time)
        self.builder.tkvariables['initHeight'].trace("w", self.on_entry_init_h)
        self.builder.tkvariables['maxHeight'].trace("w", self.on_entry_max_h)
        self.builder.tkvariables['gravity'].trace("w", self.on_entry_g)

        # Linking the canvas
        self.canvas = self.builder.get_object('draw_canvas')
        self.canvas.create_line(0, 520, 900, 520, width=50, fill='green')
        self.canvas.create_circle(PADDING_X, 475, 20, fill='red')

        # Connecting function callbacks
        builder.connect_callbacks(self)

    # Quit button funciton
    def on_click_quit(self):
        self.master.quit()

    # Height graph generator
    def on_click_height(self):
        listX, listY = GraphDataGeneratorHeight(flightTime, initHeight, 20, config.G_CONSTANT, launchAngle, initVelocity)

        fig, ax = plt.subplots()
        ax.plot(listX, listY)

        ax.set(xlabel='Time (s)', ylabel='Height (m)',
            title='Height vs Time Graph')
        ax.grid()

        #fig.savefig("Height vs Time Graph.png")
        plt.show()

    # Velocity graph generator
    def on_click_velocity(self):
        listX, listY = GraphDataGeneratorVelocity(flightTime, initVelocity, 20, config.G_CONSTANT, launchAngle)

        fig, ax = plt.subplots()
        ax.plot(listX, listY)

        ax.set(xlabel='Time (s)', ylabel='Velocity (m/s)',
            title='Velocity vs Time Graph')
        ax.grid()

        #fig.savefig("Velocity vs Time Graph.png")
        plt.show()

    # Vertical velocity graph generator
    def on_click_velocityY(self):
        listX, listY = GraphDataGeneratorVelocityY(flightTime, initVelocity, 20, config.G_CONSTANT, launchAngle)

        fig, ax = plt.subplots()
        ax.plot(listX, listY)

        ax.set(xlabel='Time (s)', ylabel='Velocity (m/s)',
            title='Vertical velocity vs Time Graph')
        ax.grid()

        #fig.savefig("Vertical velocity vs Time Graph.png")
        plt.show()

    # Calculate button function
    def on_click_calculate(self):
        self.input_handler()
        if self.passed == True:
            self.visualizer_drawer()
        else:
            pass

    # Reset button code
    def on_click_reset(self):
        config.G_CONSTANT = 9.81

        initVelocity = 0.0;
        launchAngle = 0.0;
        distanceTraveled = 0.0;
        flightTime = 0.0;
        initHeight = 0.0;
        maxHeight = 0.0;
        initG = 9.81;

        self.builder.tkvariables['initHeight'].set(0)
        self.builder.tkvariables['initVelocity'].set(0)
        self.builder.tkvariables['maxHeight'].set(0)
        self.builder.tkvariables['distanceTraveled'].set(0)
        self.builder.tkvariables['flightTime'].set(0)
        self.builder.tkvariables['launchAngle'].set(0)
        self.builder.tkvariables['gravity'].set(0)

        self.inputDistance.delete(0, tk.END)
        self.inputVelocity.delete(0, tk.END)
        self.inputMaxHeight.delete(0, tk.END)
        self.inputAngle.delete(0, tk.END)
        self.inputTime.delete(0, tk.END)
        self.inputInitHeight.delete(0, tk.END)
        self.inputG.delete(0, tk.END)

        self.inputDistance.insert(0, 0.0)
        self.inputVelocity.insert(0, 0.0)
        self.inputMaxHeight.insert(0, 0.0)
        self.inputAngle.insert(0, 0.0)
        self.inputTime.insert(0, 0.0)
        self.inputInitHeight.insert(0, 0.0)
        self.inputG.insert(0, 9.81)



    # Fuctions triggered by changes in input fields
    def on_entry_vel(self, *args):
        try:
            global initVelocity
            initVelocity = self.builder.tkvariables['initVelocity'].get()
            self.builder.tkvariables['vel_error_msg'].set("")
        except Exception as error:
            self.builder.tkvariables['vel_error_msg'].set("Invalid input! Please input a number.")

    def on_entry_angl(self, *args):
        try:
            global launchAngle
            launchAngle = self.builder.tkvariables['launchAngle'].get()
            self.builder.tkvariables['angl_error_msg'].set("")
        except Exception as error:
            self.builder.tkvariables['angl_error_msg'].set("Invalid input! Please input a number.")

    def on_entry_dist(self, *args):
        try:
            global distanceTraveled
            distanceTraveled = self.builder.tkvariables['distanceTraveled'].get()
            self.builder.tkvariables['dist_error_msg'].set("")
        except Exception as error:
            self.builder.tkvariables['dist_error_msg'].set("Invalid input! Please input a number.")

    def on_entry_time(self, *args):
        try:
            global flightTime
            flightTime = self.builder.tkvariables['flightTime'].get()
            self.builder.tkvariables['time_error_msg'].set("")
        except Exception as error:
            self.builder.tkvariables['time_error_msg'].set("Invalid input! Please input a number.")

    def on_entry_init_h(self, *args):
        try:
            global initHeight
            initHeight = self.builder.tkvariables['initHeight'].get()
            self.builder.tkvariables['init_h_error_msg'].set("")
        except Exception as error:
            self.builder.tkvariables['init_h_error_msg'].set("Invalid input! Please input a number.")

    def on_entry_max_h(self, *args):
        try:
            global maxHeight
            maxHeight = self.builder.tkvariables['maxHeight'].get()
            self.builder.tkvariables['max_h_error_msg'].set("")
        except Exception as error:
            self.builder.tkvariables['max_h_error_msg'].set("Invalid input! Please input a number.")

    def on_entry_g(self, *args):
        try:
            global initG
            initVelocity = self.builder.tkvariables['gravity'].get()
            self.builder.tkvariables['g_error_msg'].set("")
        except Exception as error:
            self.builder.tkvariables['g_error_msg'].set("Invalid input!")

    # Check conditions for each calculation case
    def VelocityHeightAngleCondition(self):
        if (initVelocity != 0 and launchAngle != 0) or (initHeight != 0 and initVelocity != 0):
            return 1
        else:
            return 0

    def AngleHeightTimeCondition(self):
        if launchAngle != 0 and flightTime != 0:
            return 1
        else:
            return 0

    def HeightTimeDistanceCondition(self):
        if flightTime != 0 and distanceTraveled != 0:
            return 1
        else:
            return 0

    def HeightTimeCondition(self):
        if flightTime != 0:
            return 1
        else:
            return 0

    # Handling input from entry
    def input_handler(self):
        config.G_CONSTANT = self.builder.tkvariables['gravity'].get()
        if self.AngleHeightTimeCondition():
            result = AngleHeightTimeCalc(launchAngle, initHeight, flightTime)
            self.passed = True
            self.inputDistance.delete(0, tk.END)
            self.inputVelocity.delete(0, tk.END)
            self.inputMaxHeight.delete(0, tk.END)
            self.inputDistance.insert(0, '{0:.3f}'.format(result[0]))
            self.inputVelocity.insert(0, '{0:.3f}'.format(result[1]))
            self.inputMaxHeight.insert(0, '{0:.3f}'.format(result[2]))
            self.builder.tkvariables['calc_error_msg'].set("Angle, initial height and time used")
        elif self.VelocityHeightAngleCondition():
            result = VelocityHeightAngleCalc(initVelocity, initHeight, launchAngle)
            self.passed = True
            self.inputDistance.delete(0, tk.END)
            self.inputTime.delete(0, tk.END)
            self.inputMaxHeight.delete(0, tk.END)
            self.inputDistance.insert(0, '{0:.3f}'.format(result[0]))
            self.inputTime.insert(0, '{0:.3f}'.format(result[1]))
            self.inputMaxHeight.insert(0, '{0:.3f}'.format(result[2]))
            self.builder.tkvariables['calc_error_msg'].set("Velocity, initial height and angle used")
        elif self.HeightTimeDistanceCondition():
            result = HeightTimeDistanceCalc(initHeight, flightTime, distanceTraveled)
            self.passed = True
            self.inputVelocity.delete(0, tk.END)
            self.inputAngle.delete(0, tk.END)
            self.inputMaxHeight.delete(0, tk.END)
            self.inputVelocity.insert(0, '{0:.3f}'.format(result[0]))
            self.inputAngle.insert(0, '{0:.3f}'.format(result[1]))
            self.inputMaxHeight.insert(0, '{0:.3f}'.format(result[2]))
            self.builder.tkvariables['calc_error_msg'].set("Distance, initial height and time used")
        elif self.HeightTimeCondition():
            self.passed = False
            result = HeightTimeCalc(initHeight, flightTime)
            self.inputMaxHeight.delete(0, tk.END)
            self.inputMaxHeight.insert(0, '{0:.3f}'.format(result))
            self.builder.tkvariables['calc_error_msg'].set("Time and initial height used")
        else:
            self.passed = False
            self.builder.tkvariables['calc_error_msg'].set("Can't calculate with input provided")

    # Drawing in canvas
    def visualizer_drawer(self):
        self.canvas.delete("all")
        main_ratio = DRAW_AREA_X / DRAW_AREA_Y

        # Hardcoded values for initial projectile positions
        startPosition = 475
        endPosition = 475

        real_x = 0
        real_y = 0

        init_vertical = initVelocity * math.sin(math.radians(launchAngle))
        timeMaxHeight = init_vertical / config.G_CONSTANT
        maxHeightXPositionTheory = timeMaxHeight * initVelocity * math.cos(math.radians(launchAngle))

        # Calculating the scaled values of distanceTraveled and maxHeight for drawing
        if distanceTraveled != 0 and maxHeight != 0:
            if distanceTraveled > maxHeight:
                ratio = distanceTraveled / maxHeight
                real_y = DRAW_AREA_X / ratio
                real_x = DRAW_AREA_X
            else:
                ratio = maxHeight / distanceTraveled
                real_y = DRAW_AREA_Y
                real_x = DRAW_AREA_Y / ratio

        if launchAngle == 90:
            maxHeightXPosition = 0
            startPosition = 475
        else:
            maxHeightXPosition = real_x * (maxHeightXPositionTheory / distanceTraveled)
            startPosition = 475 - real_y * (initHeight / maxHeight)

        ## DEBUG:
        #print(maxHeightXPositionTheory, maxHeightXPosition)
        #print(startPosition)
        #print(maxHeightXPosition)
        #print(distanceTraveled, maxHeight)
        #print(real_x, real_y)
        #print(endPosition, real_y)

        ## Redrawing canvas and adding other elements

        # Trajectory line (real_y * 2 is a hack to display correctly when initHeight = 0)
        if initHeight == 0:
            self.canvas.create_line(PADDING_X, startPosition,    maxHeightXPosition + PADDING_X, endPosition - real_y * 2,     real_x + PADDING_X, endPosition,     dash=(6,3), width=2, smooth=1)

        ## BUG: Demonstration of the line being drawn incorectly when initial position is not 0
        #self.canvas.create_line(40, 200,    55, 110,     190, 230)
        #self.canvas.create_line(40, 200,    55, 110,     190, 230, smooth=1)

        # Redrawing the projectiles and ground
        self.canvas.create_circle(PADDING_X, startPosition, 20, fill='red')
        self.canvas.create_circle(real_x + PADDING_X, endPosition, 20, fill='blue')
        self.canvas.create_line(0, 520, 900, 520, width=50, fill='green')
        self.canvas.create_line(PADDING_X, startPosition + 20, PADDING_X, 495, width=20, fill='brown')

        # Horizontal line
        self.canvas.create_line(PADDING_X, endPosition,     real_x + PADDING_X, endPosition,      width=1, arrow='both', fill='purple')

        # Vertical line
        if launchAngle == 90:
            self.canvas.create_line(maxHeightXPosition + PADDING_X, real_y + 5,      maxHeightXPosition + PADDING_X, endPosition,     width=1, arrow='both')
        self.canvas.create_line(maxHeightXPosition + PADDING_X, endPosition - real_y,      maxHeightXPosition + PADDING_X, endPosition,     width=1, arrow='both')

    # Starting the graphics
    def run(self):
        self.mainwindow.mainloop()
