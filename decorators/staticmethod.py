"""Color class

The following sites were consulted:
    http://www.99colors.net/
    https://www.webucator.com/blog/2015/03/python-color-constants-module/
"""
import os
import sys
import urllib.request

from string import hexdigits

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(self.color.upper(), None)

    @staticmethod
    def hex2rgb(hex_value):
        """Converts a hex value into an rgb one"""
        error_message = f"{hex_value} is not a valid hex value!"

        for char in hex_value[1:]:
            if char not in hexdigits:
                raise ValueError(error_message)

        if not len(hex_value) == 7 or not hex_value.startswith("#"):
            raise ValueError(error_message)

        return tuple(int(hex_value[i:i + 2], 16) for i in (1, 3, 5))

    @staticmethod
    def rgb2hex(rgb_value):
        """Converts an rgb value into a hex one"""
        error_message = f"{rgb_value} is not a valid RGB value!"

        if not isinstance(rgb_value, tuple):
            raise ValueError(error_message)

        valid = [1 for n in rgb_value if not (0 <= n <= 255)]
        if sum(valid) > 0:
            raise ValueError(error_message)

        return f"#{rgb_value[0]:02x}{rgb_value[1]:02x}{rgb_value[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return f"{self.rgb}" if self.rgb else "Unknown"