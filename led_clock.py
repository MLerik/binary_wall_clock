import datetime
from gpiozero import LED
from display import LED_Display

class LedClock():

    def __init__(self, h_p, m_p, s_p):
        self.bin_time = self._update_time()
        self.second_leds = []
        self.minute_leds = []
        self.hour_leds = []
        self.init_pins(h_p,m_p,s_p)
        self.display = LED_Display()
        return

    def init_pins(self,h_p,m_p,s_p):
        for seconds_pin in s_p:
            self.second_leds.append(LED(seconds_pin))
        for minute_pin in m_p:
            self.minute_leds.append(LED(minute_pin))
        for hour_pin in h_p:
            self.hour_leds.append(LED(hour_pin))
        return


    def _update_time(self):
        curr_time = datetime.datetime.now()
        time = []
        time.append([int(x) for x in '{0:06b}'.format(curr_time.second)])
        time.append([int(x) for x in '{0:06b}'.format(curr_time.minute)])
        time.append([int(x) for x in '{0:06b}'.format(curr_time.hour)])
        time.append([int(x) for x in '{0:06b}'.format(curr_time.day)])
        time.append([int(x) for x in '{0:06b}'.format(curr_time.month)])
        time.append([int(x) for x in '{0:06b}'.format(curr_time.year-2000)])
        return time

    def display_time(self,display='LEDScreen'):
        self.bin_time = self._update_time()
        wide = False # defines one or two LEDS for display
        if display == 'LEDScreen':
            if not wide:
                for frame_updates in range(30):
                    for time_slot in range(len(self.bin_time)):
                        for bit in range(len( self.bin_time[time_slot])):
                            if self.bin_time[time_slot][bit] == 1:
                                self.display.light_led(6-time_slot,6-bit,0.001)
            else:
                for frame_updates in range(30):
                    for time_slot in range(3):
                        for bit in range(6):
                            if self.bin_time[time_slot][bit] == 1:
                                coord = 2*time_slot
                                self.display.light_led(7-coord, 5 - bit, 0.0001)
                                self.display.light_led(7-coord-1, 5 - bit, 0.0001)

        else:
            for time_slot in range(3):
                if time_slot == 0:
                    current_leds = self.second_leds
                elif time_slot == 1:
                    current_leds = self.minute_leds
                else:
                    current_leds = self.hour_leds

                bin_position = 0
                for pin in range(len(current_leds)):
                    bin_value = self.bin_time[time_slot][bin_position]
                    if bin_value > 0:
                        current_leds[bin_position].on()
                    else:
                        current_leds[bin_position].off()
                    bin_position += 1
        return


