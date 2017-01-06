#JS/try with pigpio library
#

import pigpio


pi = pigpio.pi()



#Left
pi.set_mode(18, pigpio.OUTPUT) # GPIO.setup(18,  GPIO.OUT) PWM
pi.set_mode( 4, pigpio.OUTPUT) # GPIO.setup(4,   GPIO.OUT)
pi.set_mode(17, pigpio.OUTPUT) # GPIO.setup(17,  GPIO.OUT) 


#Right
pi.set_mode( 2, pigpio.OUTPUT) # GPIO.setup(2,  GPIO.OUT) PWM
pi.set_mode(24, pigpio.OUTPUT) # GPIO.setup(24,   GPIO.OUT)
#pi.set_mode(28, pigpio.OUTPUT) # GPIO.setup(24,   GPIO.OUT)

def clockwise():
    pi.write( 4, 1)
    pi.write(17, 0)
    pi.write(24, 1)
    #pi.write(28, 0)
    print("Counter_Clockwise")

def counter_clockwise():
    pi.write( 4, 0)
    pi.write(17, 1)
    pi.write(24, 0)
    #pi.write(28, 1)
    print("Counter_Clockwise")

clockwise()

pi.set_PWM_dutycycle(2, 255)
pi.set_PWM_dutycycle(18, 255)

#while True:
    #cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    #direction = cmd[0]
    #if direction == "f":
        #clockwise()
        #print("Clockwise")
#        
    #else: 
        #counter_clockwise()
#    
    #speed = int(cmd[1]) * 11
    #p.ChangeDutyCycle(speed)

#GPIO.cleanup()
