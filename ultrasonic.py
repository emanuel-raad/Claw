import RPi.GPIO as GPIO
import time
from scipy import median


'''
Class to interface with the HC-SR04 ultrasonic sensor and the raspberry pi
'''
class Ultrasonic:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    '''
    sampleSize: number of readings to make
    waitTime: time to wait between readings, in seconds
    return: median of the measured distances, in centimeters
    '''
    def getDistance(self, sampleSize = 10, waitTime = 0.00001):
        distances = []
        time.sleep(2)

        for i in range(0, sampleSize):
            # set Trigger to HIGH
            GPIO.output(self.trig, True)

            # set Trigger after specificied wait time to LOW
            time.sleep(waitTime)
            GPIO.output(self.trig, False)

            StartTime = time.time()
            StopTime = time.time()

            # save StartTime
            while GPIO.input(self.echo) == 0:
                StartTime = time.time()

            # save time of arrival
            while GPIO.input(self.echo) == 1:
                StopTime = time.time()

            # time difference between start and arrival
            TimeElapsed = StopTime - StartTime

            # multiply with the speed of sounds(34300 cm/s)
            # and divide by 2, because the signal has to travel there and back
            distance = (TimeElapsed * 34300) / 2

            # Upper and lower bound on distance, 2cm to 500cm
            if ((distance > 2) and (distance < 500)):
                distances.append(distance)

        return median(distances)


def main():
    # Create an ultrasonic object.
    # d = Ultrasonic(trig_pin, echo_pin)
    d = Ultrasonic(23, 24)

    # Use d.getDistance() to read the distance in centimeters
    # Each run will take about 2 seconds, because the sensor takes time to settle

    # Example usage below, in a while loop. Exit using Ctrl+C
    try:
        while True:
            print d.getDistance()
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()