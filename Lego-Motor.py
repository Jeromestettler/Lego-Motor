#JS/try with pigpio library
#

import pigpio


pi = pigpio.pi()



#Left
pi.set_mode(18, pigpio.OUTPUT) # GPIO.setup(18,  GPIO.OUT)
pi.set_mode( 4, pigpio.OUTPUT) # GPIO.setup(4,   GPIO.OUT)
pi.set_mode(17, pigpio.OUTPUT) # GPIO.setup(17,  GPIO.OUT) 


#Right
pi.set_mode( 2, pigpio.OUTPUT) # GPIO.setup(2,  GPIO.OUT)
pi.set_mode(24, pigpio.OUTPUT) # GPIO.setup(24,   GPIO.OUT)
pi.set_mode(28, pigpio.OUTPUT) # GPIO.setup(28,  GPIO.OUT) 


p = GPIO.PWM(2,20)
p = GPIO.PWM(18,20)



p.start(0)


def clockwise():
    GPIO.output(4, True)
    GPIO.output(17, False)
    print("Counter_Clockwise")
    GPIO.output(24, True)
    GPIO.output(28, False)
    print("Counter_Clockwise")
    
def counter_clockwise():
    GPIO.output(4, False)
    GPIO.output(17, True)
    print("Counter_Clockwise")
    GPIO.output(24, False)
    GPIO.output(28, True)
    print("Counter_Clockwise")
clockwise()
 
while True:
    cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "f":
        clockwise()
        print("Clockwise")
        
    else: 
        counter_clockwise()
    
    speed = int(cmd[1]) * 11
    p.ChangeDutyCycle(speed)

GPIO.cleanup()
