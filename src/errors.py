#!/usr/bin/env python3

"""
Custom Exceptions
"""


class IncorretTimeFormatException(Exception):
    """
    Custom exception for raising time format error
    """

    message = "Incorrect time format. Expected hh:mm "
