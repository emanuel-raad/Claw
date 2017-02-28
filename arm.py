import RPi.GPIO as GPIO
import time

pin = 12

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)


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
        self.p.ChangeDutyCycle(duty)
        time.sleep(sleep)

    def setDebug(self, debug):
        self.debug = debug


def main():
    initGPIO()
    print "Hello World!"
    armServo = Motor(12)
    armServo.setDebug(True)
    armServo.start(Motor.OPEN)
    time.sleep(1)
    armServo.p.ChangeDutyCycle(0)


    servo2 = Motor(40)
    servo2.start(7.5)
    time.sleep(1)
    servo2.p.ChangeDutyCycle(0)

    armServo.p.ChangeDutyCycle(Motor.OPEN)
    time.sleep(1)

    armServo.p.stop()
    servo2.p.stop()
    GPIO.cleanup()

    """
    try:
        while True:
            p = float(raw_input("pos "))
            t = float(raw_input("sleep "))
            #armServo.turnToAndSleep(Motor.OPEN, 3)
            #armServo.turnToAndSleep(Motor.CENTER, 3)
            armServo.turnToAndSleep(p, t)
    except KeyboardInterrupt:
        armServo.p.stop()
        GPIO.cleanup()
    """
if __name__=="__main__":
    main()
