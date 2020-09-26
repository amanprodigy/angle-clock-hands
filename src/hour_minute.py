#!/usr/bin/env python3

"""
Tells the angle difference between two hands of the clock
"""

from .validators import validate_time
from .constants import RATE_HOUR_HAND, RATE_MINUTE_HAND


def angle_between_minute_hour_hands(time_in_24_hr: str) -> float:
    """
    Tells the angle b/w minute and hour hands
    for a given time in the 24 hour format
    """
    # hh range 00 to 12
    # mm range 00 to 59
    # 23:59 is the last time and 00:00 is the first time

    validate_time(time_in_24_hr)

    hh, mm = [int(x) for x in time_in_24_hr.split(":")]

    total_minutes_traversed = hh * 60 + mm

    hour_degree_movement = RATE_HOUR_HAND * total_minutes_traversed
    minute_degree_movement = RATE_MINUTE_HAND * total_minutes_traversed

    # Get the absolute angle difference in a maximum span of 360 degrees
    angle_diff = abs(minute_degree_movement - hour_degree_movement) % 360

    # Convert reflex angle to obtuse/acute angle
    if angle_diff > 180:
        return 360 - angle_diff

    return angle_diff
