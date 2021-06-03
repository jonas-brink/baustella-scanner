import RPi.GPIO as GPIO
import time


class beeper:
    def __init__(self):
        self.pin = 23
        self.tune = 1000
        self.wartezeit = 0.2

        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.tune)

    def starteTon(self):
        self.pwm.start(50)
        time.sleep(self.wartezeit)
        self.pwm.stop()
        GPIO.cleanup()


