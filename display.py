import RPi.GPIO as IO
import time  # calling for time to provide delays in program
import numpy as np
from PIL import Image

x = 1
y = 1



class LED_Display():

    def __init__(self):
        self.pos_pins = [12, 22, 27, 25, 17, 24, 23, 18]
        self.neg_pins = [21, 20, 26, 16, 19, 13, 6, 5]
        IO.setmode(IO.BCM)  # programming the GPIO by BCM pin numbers. (like PIN29 as'GPIO5')
        IO.setup(12, IO.OUT)  # initialize GPIO12 as an output.
        IO.setup(22, IO.OUT)  # initialize GPIO22 as an output.
        IO.setup(27, IO.OUT)
        IO.setup(25, IO.OUT)
        IO.setup(17, IO.OUT)
        IO.setup(24, IO.OUT)
        IO.setup(23, IO.OUT)
        IO.setup(18, IO.OUT)
        IO.setup(21, IO.OUT)
        IO.setup(20, IO.OUT)
        IO.setup(26, IO.OUT)
        IO.setup(16, IO.OUT)
        IO.setup(19, IO.OUT)
        IO.setup(13, IO.OUT)
        IO.setup(6, IO.OUT)
        IO.setup(5, IO.OUT)
        IO.setwarnings(False)  # do not show any warnings
        self.clear_display()

    def clear_display(self):
        """
        Clear all leds on display
        :return:
        """
        for i in range(8):
            IO.output(self.pos_pins[7 - i], 1)
            IO.output(self.neg_pins[7 - i], 0)

    def fill_display(self):
        """
        light up all the leds of display
        :return:
        """
        for i in range(8):
            IO.output(self.pos_pins[i], 0)
            IO.output(self.neg_pins[i], 1)

    def light_led(self, x, y, sleep_time=-1):
        """
        light a specific LED light

        :param x: x-coordinate of LED
        :param y: y-coordinate of LED
        :param sleep_time: Duration of LED light pulse
        :return:
        """
        IO.output(self.pos_pins[7 - y], 0)
        IO.output(self.neg_pins[7 - x], 1)
        if sleep_time > 0:
            time.sleep(sleep_time)
            IO.output(self.pos_pins[7 - y], 1)
            IO.output(self.neg_pins[7 - x], 0)

    def display_matrix(self, mat, steps):
        """
        Display a 8x8 Matrix on display

        :param mat:
        :param steps:
        :return:
        """

        lighted_leds = []
        for y in range(8):
            for x in range(8):
                if mat[y, x] >= 1:
                    lighted_leds.append((x, y))
        if len(lighted_leds) < 1:
            time.sleep(0.2)

        for t in range(steps):
            for i in range(len(lighted_leds)):
                self.light_led(lighted_leds[i][0], 7 - lighted_leds[i][1], 0.0001)

    def scroll_matrix(self, matrix, sweeps, speed):
        """
        Scroll matrix thrgouh display

        :param matrix:
        :param sweeps:
        :param speed:
        :return:
        """
        for sw in range(sweeps):
            for step in range(np.shape(matrix)[1] - 8):
                curr_window = matrix[:, step:step + 8]
                self.display_matrix(curr_window, speed)

    def scroll_text(self, text, sweeps, speed):
        """
        This is a function to scroll text across a 8x8 LED Display
        :param text: Input text that should scroll on display
        :param sweeps: Number of times the text should scroll
        :param speed: Speed of scroll (Larger number is smaller speed)
        :return: returns nothing
        """
        initial = True
        for C in text:
            if C == " ":
                C = "Space"
            if C == "*":
                C = "star"
            if C == "#":
                C = "heart"
            letter_im = Image.open("./imgs/" + C + ".bmp")
            letter_array = 1 - np.clip(np.array(letter_im), 0, 1)
            if initial:
                word = letter_array
                initial = False
            else:
                word = np.concatenate((word, letter_array), axis=1)
        self.scroll_matrix(word, sweeps, speed)
