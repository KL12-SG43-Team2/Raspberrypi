import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)
switch = 23
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

steam = open('Project.py')

while True:
    if GPIO.input(switch) == GPIO.HIGH:
        while True:
            exec(steam)
    break
