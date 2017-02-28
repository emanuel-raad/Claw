import RPi.GPIO as GPIO
import time

pin = 40

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

def cleanupGPIO():
    armServo.p.stop()
    GPIO.cleanup()

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
        if (self.debug):
            print "Going to {}. Sleeping for {}".format(duty, sleep)
        print "here"
        self.p.ChangeDutyCycle(duty)
        time.sleep(sleep)

    def setDebug(self, debug):
        self.debug = debug


def main():
    initGPIO()
    print "Hello World!"
    armServo = Motor(pin)
    armServo.setDebug(True)
    armServo.start(Motor.CENTER)

    try:
        while True:
            armServo.turnToAndSleep(Motor.OPEN, 3)
            armServo.turnToAndSleep(Motor.CENTER, 3)
    except KeyboardInterrupt:
        cleanupGPIO()

if __name__=="__main__":
    main()
