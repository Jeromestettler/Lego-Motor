#JS/try with RPIO library. from pythonhoset.org/RPIO
#
#import RPi

#servo = PWM.Servo()
 
#servo.set_servo(17, 1200)
 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

##Left
GPIO.setup(18,  GPIO.OUT)
GPIO.setup(4,   GPIO.OUT)
GPIO.setup(17,  GPIO.OUT)

##Right
GPIO.setup(2,   GPIO.OUT)
GPIO.setup(24,  GPIO.OUT)
GPIO.setup(28,  GPIO.OUT)

p = GPIO.PWM(2,20)
p = GPIO.PWM(18,20)

p.start(0)

def clockwise():
    GPIO.output(4, True)
    GPIO.output(17, False)
    GPIO.output(24, True)
    GPIO.output(28, False)
    print("Clockwise")
    
def counter_clockwise():
    GPIO.output(4, False)
    GPIO.output(17, True)
    GPIO.output(24, False)
    GPIO.output(28, True)
    print("Counter_Clockwise")
    
    
clockwise()
 
while True:
    cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "f":
        clockwise()
        
    else: 
        counter_clockwise()
    
    speed = int(cmd[1]) * 11
    p.ChangeDutyCycle(speed)

GPIO.cleanup()
