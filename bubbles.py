from gpiozero import AngularServo
from gpiozero import LED
from time import sleep

#setting up servo and fan.
servo = AngularServo(4, min_angle=-90, max_angle=90)
fan = LED(17)

theDangle = -90


while True:
    theDangle = -90
    servo.angle = theDangle
    sleep(0.5)
    #This for loop is used to slow down the servo, previously it threw the bubble mix all over the place.
    for i in range(19):
        servo.angle = theDangle
        print(theDangle)
        theDangle += 10
        sleep(0.1)
    #starting the fan
    fan.on()
    #giving the fan time to blow some bubbles.
    sleep(2)
    #shuting the fan off.
    fan.off()
    #giving the fan some time to spin down.
    sleep(2)
