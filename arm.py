import RPi.GPIO as GPIO
import time

pin = 12

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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)

    print "Hello World!"

    armServo = Motor(40)
    armServo.setDebug(True)
    armServo.start(Motor.OPEN)
    armServo.turnToAndSleep(7.5, 5)
    armServo.p.ChangeDutyCycle(0)
    time.sleep(3)

    clawServo = Motor(12)
    clawServo.setDebug(True)
    clawServo.start(MOTOR.CLOSE)
    time.sleep(1)
    clawServo.turnToAndSleep(MOTOR.OPEN, 0)

    time.sleep(5)
    armServo.turnToAndSleep(12.5, 5)

    armServo.p.stop()
    clawServo.p.stop()
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
