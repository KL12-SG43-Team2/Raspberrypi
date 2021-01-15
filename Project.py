import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
import time
from apa102_pi.driver import apa102

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
sr04_trig = 20
sr04_echo = 21
led = 17
switch = 23
servo = Servo(25)
clock_pin = 5
latch_pin = 6
data_pin = 13
GPIO.setup(sr04_trig, GPIO.OUT)
GPIO.setup(sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup( led, GPIO.OUT )
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)

strip = apa102.APA102(num_led=8, mosi=10, sclk=11, order='rbg')
strip.set_global_brightness(31)

def shift(clock_pin, latch_pin, data_pin):
    for y in range(8):
        x = 1
        GPIO.setup(data_pin, GPIO.OUT)
        GPIO.setup(latch_pin, GPIO.OUT)
        GPIO.setup(clock_pin, GPIO.OUT)

        for i in range(1):
            for y in range(1):
                GPIO.output(data_pin, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(clock_pin,  GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(clock_pin, GPIO.LOW)
                GPIO.output(data_pin, GPIO.LOW)
                GPIO.output(latch_pin, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(latch_pin, GPIO.LOW)


            for y in range(1):
                GPIO.output(data_pin, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(clock_pin, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(clock_pin, GPIO.LOW)
                GPIO.output(data_pin, GPIO.LOW)
                GPIO.output(latch_pin, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(latch_pin, GPIO.LOW)

def close():
    strip.set_global_brightness(31)
    strip.set_pixel_rgb(0, 0xFF0000)
    strip.set_pixel_rgb(1, 0xFF0000)
    strip.set_pixel_rgb(2, 0xFF0000)
    strip.set_pixel_rgb(3, 0xFF0000)
    strip.set_pixel_rgb(4, 0xFF0000)
    strip.set_pixel_rgb(5, 0xFF0000)
    strip.set_pixel_rgb(6, 0xFF0000)
    strip.set_pixel_rgb(7, 0xFF0000)
    strip.show()

def sr04(trig_pin, echo_pin,):

    GPIO.output(trig_pin, True)
    time.sleep(0.000001)
    GPIO.output(trig_pin, False)

    while GPIO.input(echo_pin) == 0:
      Start = time.time()
    while GPIO.input(echo_pin) == 1:
      Stop = time.time()

    Totaal = Stop - Start
    print(Totaal)

    Afstand = (Totaal * 34300) / 2

    if Afstand < 20:
        close()
        servo.min()
        sleep(1)

    elif Afstand > 20:
        servo.max()
        sleep(1)
        strip.clear_strip()

    return Afstand

while True:
    if GPIO.input(switch) == GPIO.HIGH:
        shift(clock_pin,latch_pin,data_pin)
        while True:
            print(sr04(sr04_trig, sr04_echo,))
            time.sleep(0.5)








