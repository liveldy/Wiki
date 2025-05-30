from machine import Pin,PWM
from time import sleep_ms


class BUZZER:
    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))

    def play(self, melodies, wait, duty):
        for note in melodies:
            print("note:{}".format(note))
            if note:
                self.pwm.freq(note)
            self.pwm.duty(duty)
            sleep_ms(wait)
        self.pwm.duty(0)

