from __future__ import print_function
import string
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

class TextConverter:
    def __init__(self):
        return

    def char_to_pixels(text, path="/usr/share/fonts/truetype/freefont/FreeMono.ttf", fontsize=8):
        """
        Based on https://stackoverflow.com/a/27753869/190597 (jsheperd)
        """
        font = ImageFont.truetype(path, fontsize)
        w, h = font.getsize(text)
        h *= 2
        image = Image.new('L', (w, h), 1)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font)
        arr = np.asarray(image)
        arr = np.where(arr, 0, 1)
        arr = arr[(arr != 0).any(axis=1)]
        return arr