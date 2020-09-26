#!/usr/bin/env python3

"""
Validators for the app
"""

import time
from .errors import IncorretTimeFormatException


def validate_time(time_in_24_hr: str) -> bool:
    """
    Validates if the given string is of valid 24 hour format
    """
    try:
        time.strptime(time_in_24_hr, "%H:%M")
        return True
    except ValueError:
        raise IncorretTimeFormatException() from None
