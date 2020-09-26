#!/usr/bin/env python3

"""
Application Tests
"""

import unittest
from src.hour_minute import angle_between_minute_hour_hands as angle
from src.errors import IncorretTimeFormatException


class TestAngleBetweenHourMinuteHands(unittest.TestCase):
    """
    Tests the Angle at Time App
    """

    GOOD_CASES = {
        "6:15": 97.5,
        "3:15": 7.5,
        "00:00": 0.0,
        "03:00": 90,
        "5:30": 15.0,
    }

    BAD_CASES = {
        "6:15": 99.5,
        "3:15": 17.5,
        "00:00": 180.0,
        "03:00": 270,
        "5:30": 145.0,
    }

    INCORRECT_TIMES = [
        "24:15",
        "-56:00",
        "+24:15pm",
        "01:15am",
        "00:00pm",
    ]

    def test_good_cases(self):
        for time_string, expected_angle in self.GOOD_CASES.items():
            self.assertEqual(angle(time_string), expected_angle)

    def test_bad_cases(self):
        for time_string, expected_angle in self.BAD_CASES.items():
            self.assertNotEqual(angle(time_string), expected_angle)

    def test_incorrect_times(self):
        for time_string in self.INCORRECT_TIMES:
            self.assertRaises(IncorretTimeFormatException, angle, time_string)
