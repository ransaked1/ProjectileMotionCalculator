import unittest

import os
import sys
sys.path.append('../')

from src.AngleHeightTimeCalc import AngleHeightTimeCalc
from src.HeightTimeDistanceCalc import HeightTimeDistanceCalc
from src.VelocityHeightAngleCalc import VelocityHeightAngleCalc
from src.HeightTimeCalc import HeightTimeCalc

class ProjectUnitTest(unittest.TestCase):
    #Angle Height Time result format [distance, speed, max_height]
    def test_AngleHeightTime_45_0_10(self):
        result = AngleHeightTimeCalc(45, 0, 10)
        self.assertEqual([490, 69, 122], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_45_10_10(self):
        result = AngleHeightTimeCalc(45, 10, 10)
        self.assertEqual([480, 67, 127], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_90_10_10(self):
        result = AngleHeightTimeCalc(90, 10, 10)
        self.assertEqual([0, 48, 127], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_0_10_10(self):
        result = AngleHeightTimeCalc(0, 10, 10)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    def test_AngleHeightTime_45_10_0(self):
        result = AngleHeightTimeCalc(45, 10, 0)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    #Height Time Distance result format [speed, angle, max_height]
    def test_HeightTimeDistance_10_10_15(self):
        result = HeightTimeDistanceCalc(10, 10, 15)
        self.assertEqual([49, 88, 132], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_0_5_30(self):
        result = HeightTimeDistanceCalc(0, 5, 30)
        self.assertEqual([25, 76, 30], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_5_10_150(self):
        result = HeightTimeDistanceCalc(5, 10, 150)
        self.assertEqual([51, 72, 127], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_40_0_10(self):
        result = HeightTimeDistanceCalc(40, 0, 10)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    def test_HeightTimeDistance_45_10_0(self):
        result = HeightTimeDistanceCalc(45, 10, 0)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    #Velocity Height Angle result format [distance, time, max_height]
    def test_VelocityHeightAngle_10_10_45(self):
        result = VelocityHeightAngleCalc(10, 10, 45)
        self.assertEqual([16, 2, 12], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_40_0_77(self):
        result = VelocityHeightAngleCalc(40, 0, 77)
        self.assertEqual([71, 7, 77], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_40_0_28(self):
        result = VelocityHeightAngleCalc(40, 0, 28)
        self.assertEqual([135, 3, 17], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_0_0_28(self):
        result = VelocityHeightAngleCalc(0, 0, 28)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    def test_VelocityHeightAngle_40_0_0(self):
        result = VelocityHeightAngleCalc(40, 0, 0)
        self.assertEqual([0, 0, 0], [int(result[0]), int(result[1]), int(result[2])])

    #Height Time result format max_height
    def test_HeightTime_0_10(self):
        result = HeightTimeCalc(0, 10)
        self.assertEqual(122, int(result))

    def test_HeightTime_0_1(self):
        result = HeightTimeCalc(0, 1)
        self.assertEqual(1, int(result))

    def test_HeightTime_10_10(self):
        result = HeightTimeCalc(10, 10)
        self.assertEqual(127, int(result))

    def test_HeightTime_100_10(self):
        result = HeightTimeCalc(100, 10)
        self.assertEqual(177, int(result))

    def test_HeightTime_10_0(self):
        result = HeightTimeCalc(10, 0)
        self.assertEqual(0, int(result))

if __name__ == '__main__':
    unittest.main()
