from led_clock import LedClock
from time import sleep
from display import LED_Display
from PIL import Image
import numpy as np
import datetime

im1 = Image.open("./imgs/left_smiley.bmp")
im2 = Image.open("./imgs/straight_smiley.bmp")
im3 = Image.open("./imgs/right_smiley.bmp")
im4 = Image.open("./imgs/sun.bmp")
im5 = Image.open("./imgs/line.bmp")

p1 = 1.-np.clip(np.array(im1),0,1)
p2 = 1.-np.clip(np.array(im2),0,1)
p3 = 1.-np.clip(np.array(im3),0,1)
p4 = 1.-np.clip(np.array(im4),0,1)
txt_matrix = 1.-np.clip(np.array(im5),0,1)
im_array = [p1,p2,p3,p4]

hour_pins = [11,9,10,27,22,4]
minute_pins = [26,19,13,15,14,17]
second_pins = [21,20,16,12,7,25]
bin_clock = LedClock(hour_pins, minute_pins, second_pins)
led_display = LED_Display()
led_display.scroll_text("HEYSAAN ERIK OCH AKE ", 1, 100)
while True:
    bin_clock.display_time()


    currtime = datetime.datetime.now()
    if currtime.second == 0:
        im_idx = np.random.randint(0,len(im_array))
        led_display.scroll_matrix(txt_matrix,1,50)



