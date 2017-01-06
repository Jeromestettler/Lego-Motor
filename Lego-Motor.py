#JS/try with RPIO library. from pythonhoset.org/RPIO
#
#import RPi

#servo = PWM.Servo()
 
#servo.set_servo(17, 1200)
 
from RPIO import PWM
#import RPIO



#GPIO.setmode(GPIO.BCM)

###Left
#RPIO.setup(18,  RPIO.OUT)
#RPIO.setup(4,   RPIO.OUT)
#RPIO.setup(17,  RPIO.OUT)

###Right
#RPIO.setup(2,   RPIO.OUT)
#RPIO.setup(24,  RPIO.OUT)
#RPIO.setup(28,  RPIO.OUT)

#servo = PWM.Servo()
#servo.set_servo(17, 1200)



#p = GPIO.PWM(2,20)
#p = GPIO.PWM(18,20)

#p.start(0)


#def clockwise():
    #GPIO.output(4, True)
    #GPIO.output(17, False)
    #print("Counter_Clockwise")
    #GPIO.output(24, True)
    #GPIO.output(28, False)
    #print("Counter_Clockwise")
    
#def counter_clockwise():
    #GPIO.output(4, False)
    #GPIO.output(17, True)
    #print("Counter_Clockwise")
    #GPIO.output(24, False)
    #GPIO.output(28, True)
    #print("Counter_Clockwise")
#clockwise()
 
#while True:
    #cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    #direction = cmd[0]
    #if direction == "f":
        #clockwise()
        #print("Clockwise")
        
    #else: 
        #counter_clockwise()
    
    #speed = int(cmd[1]) * 11
    #p.ChangeDutyCycle(speed)

#GPIO.cleanup()
