from threading import Thread
import time
import RPi.GPIO as GPIO

class Motor(Thread):
    CENTER = 7.5
    OPEN = 12.5
    CLOSE = 2.5

    def __init__(self, port, name, startPosition):
        Thread.__init__(self)
        self.port = port
        self.frequency = 50
        self.name = name
        self.p = GPIO.PWM(self.port, self.frequency)
        self.p.start(startPosition)
        self.position = startPosition
        self.running = True
        self.debug = True

    def run(self):
        while self.running:
            self.p.ChangeDutyCycle(self.position)
            # print("Position: {}").format(self.position)
            time.sleep(1)

    def setRunning(self, isRunning):
        self.running = isRunning

    def setPosition(self, position):
        self.position = position

    def turnToAndSleep(self, duty, sleep):
        if (self.debug):
            print "{}: Going to {}. Sleeping for {}".format(self.name, duty, sleep)
        self.p.ChangeDutyCycle(duty)
        time.sleep(sleep)

    def stop(self):
        self.running = False
        self.position = 0
        # self.p.stop()

    def setDebug(self, debug):
        self.debug = debug


def main():
    PIN_ARM = 40
    PIN_CLAW = 12

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_ARM, GPIO.OUT)

    armMotor = Motor(PIN_ARM, 'arm', Motor.OPEN)
    armMotor.start()
    time.sleep(2)
    armMotor.setPosition(Motor.CLOSE)
    time.sleep(2)

if __name__ == "__main__":
    main()