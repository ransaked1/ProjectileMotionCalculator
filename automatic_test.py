import unittest

import os
import sys
sys.path.append('src/')

from AngleHeightTimeCalc import AngleHeightTimeCalc
from HeightTimeDistanceCalc import HeightTimeDistanceCalc
from VelocityHeightAngleCalc import VelocityHeightAngleCalc
from HeightTimeCalc import HeightTimeCalc

import config

class ProjectUnitTest(unittest.TestCase):
    # Angle Height Time result format [distance, speed, max_height]
    def test_AngleHeightTime_45_0_10(self):
        config.G_CONSTANT = 9.81
        result = AngleHeightTimeCalc(45, 0, 10)
        self.assertEqual([490, 69, 122], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_45_10_10(self):
        config.G_CONSTANT = 9.81
        result = AngleHeightTimeCalc(45, 10, 10)
        self.assertEqual([480, 67, 127], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_90_10_10(self):
        config.G_CONSTANT = 9.81
        result = AngleHeightTimeCalc(90, 10, 10)
        self.assertEqual([0, 48, 127], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_0_10_10(self):
        config.G_CONSTANT = 9.81
        result = AngleHeightTimeCalc(0, 10, 10)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_45_10_0(self):
        config.G_CONSTANT = 9.81
        result = AngleHeightTimeCalc(45, 10, 0)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    # Height Time Distance result format [speed, angle, max_height]
    def test_HeightTimeDistance_10_10_15(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeDistanceCalc(10, 10, 15)
        self.assertEqual([49, 88, 132], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_0_5_30(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeDistanceCalc(0, 5, 30)
        self.assertEqual([25, 76, 30], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_5_10_150(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeDistanceCalc(5, 10, 150)
        self.assertEqual([51, 72, 127], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_40_0_10(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeDistanceCalc(40, 0, 10)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_45_10_0(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeDistanceCalc(45, 10, 0)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    # Velocity Height Angle result format [distance, time, max_height]
    def test_VelocityHeightAngle_10_10_45(self):
        config.G_CONSTANT = 9.81
        result = VelocityHeightAngleCalc(10, 10, 45)
        self.assertEqual([16, 2, 12], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_40_0_77(self):
        config.G_CONSTANT = 9.81
        result = VelocityHeightAngleCalc(40, 0, 77)
        self.assertEqual([71, 7, 77], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_40_0_28(self):
        config.G_CONSTANT = 9.81
        result = VelocityHeightAngleCalc(40, 0, 28)
        self.assertEqual([135, 3, 17], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_0_0_28(self):
        config.G_CONSTANT = 9.81
        result = VelocityHeightAngleCalc(0, 0, 28)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_40_0_0(self):
        config.G_CONSTANT = 9.81
        result = VelocityHeightAngleCalc(40, 0, 0)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    #Height Time result format max_height
    def test_HeightTime_0_10(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeCalc(0, 10)
        self.assertEqual(122, int(result))

    def test_HeightTime_0_1(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeCalc(0, 1)
        self.assertEqual(1, int(result))

    def test_HeightTime_10_10(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeCalc(10, 10)
        self.assertEqual(127, int(result))

    def test_HeightTime_100_10(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeCalc(100, 10)
        self.assertEqual(177, int(result))

    def test_HeightTime_10_0(self):
        config.G_CONSTANT = 9.81
        result = HeightTimeCalc(10, 0)
        self.assertEqual(0, int(result))

    # Angle Height Time with Gravity result format [distance, speed, max_height]
    def test_AngleHeightTimeGravity_45_0_10_6(self):
        config.G_CONSTANT = 6
        result = AngleHeightTimeCalc(45, 0, 10)
        self.assertEqual([300, 42, 75], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTimeGravity_45_10_10_14(self):
        config.G_CONSTANT = 14
        result = AngleHeightTimeCalc(45, 10, 10)
        self.assertEqual([690, 97, 180], [int(result[0]), int(result[1]), int(result[2])])

    # Height Time Distance with Gravity result format [speed, angle, max_height]
    def test_HeightTimeDistanceGravity_10_10_15_8(self):
        config.G_CONSTANT = 8
        result = HeightTimeDistanceCalc(10, 10, 15)
        self.assertEqual([40, 87, 110], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistanceGravity_0_5_30_11(self):
        config.G_CONSTANT = 11
        result = HeightTimeDistanceCalc(0, 5, 30)
        self.assertEqual([28, 77, 34], [int(result[0]), int(result[1]), int(result[2])])

    # Velocity Height Angle with Gravity result format [distance, time, max_height]
    def test_VelocityHeightAngleGravity_10_10_45_3(self):
        config.G_CONSTANT = 3
        result = VelocityHeightAngleCalc(10, 10, 45)
        self.assertEqual([41, 5, 18], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngleGravity_40_0_77_13(self):
        config.G_CONSTANT = 13
        result = VelocityHeightAngleCalc(40, 0, 77)
        self.assertEqual([53, 5, 58], [int(result[0]), int(result[1]), int(result[2])])

    # Height Time result format max_height
    def test_HeightTimeGravity_0_10_8(self):
        config.G_CONSTANT = 8
        result = HeightTimeCalc(0, 10)
        self.assertEqual(100, int(result))

    def test_HeightTimeGravity_0_4_15(self):
        config.G_CONSTANT = 15
        result = HeightTimeCalc(0, 4)
        self.assertEqual(30, int(result))


if __name__ == '__main__':
    unittest.main()
