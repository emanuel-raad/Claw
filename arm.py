import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 50)
p.start(7.5)

class Motor()

    CENTER = 7.5
    OPEN = 12.5
    CLOSE = 2.5

    def __init__(self, port):
        self.port = port
        self.frequency = 50
        self.p = GPIO.PWM(self.port, self.frequency)

    def start(self, duty):
        self.p.start(duty)

    def turnToAndSleep(self, duty, sleep):
        self.p.ChanceDutyCycle(duty, sleep)


def main():
    print "Hello World!"

    try:
        while True:
            p.ChangeDutyCycle(7.5)  # turn towards 90 degree
            time.sleep(1) # sleep 1 second
            p.ChangeDutyCycle(2.5)  # turn towards 0 degree
            time.sleep(1) # sleep 1 second
            p.ChangeDutyCycle(12.5) # turn towards 180 degree
            time.sleep(1) # sleep 1 second
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

if __name__=="__main__":
    main()
