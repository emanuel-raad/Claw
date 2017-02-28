import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 50)
p.start(7.5)

class Motor():
    CENTER = 7.5
    OPEN = 12.5
    CLOSE = 2.5

    def __init__(self, port):
        self.port = port
        self.frequency = 50
        self.p = GPIO.PWM(self.port, self.frequency)
        self.debug = False

    def start(self, duty):
        self.p.start(duty)

    def turnToAndSleep(self, duty, sleep):
        if (debug):
            print "Going to {}. Sleeping for {}".format(duty, sleep)
        self.p.ChangeDutyCycle(duty)
        time.sleep(sleep)

    def setDebug(self, debug):
        self.debug = debug


def main():
    print "Hello World!"
    armServo = Motor(40)
    armServo.setDebug(True)
    armServo.start(Motor.CENTER)

    try:
        while True:
            print "OPEN"
            armServo.turnToAndSleep(Motor.OPEN, 3)
            print "CLOSE"
            armServo.turnToAndSleep(Motor.CENTER, 3)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

if __name__=="__main__":
    main()
