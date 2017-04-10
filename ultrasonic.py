import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library

class Ultrasonic:
  def __init__(self, trig, echo):
    self.trig = trig
    self.echo = echo
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.trig, GPIO.OUT)
    GPIO.setup(self.echo, GPIO.IN)

  def getDistance(self, sampleSize = 10, waitTime = 0.00001):
    # set Trigger to HIGH
    GPIO.output(self.trig, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
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
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance


def main():
  print "hi"
  d = Ultrasonic(23, 24)

  while True:
    print d.getDistance()
    time.sleep(1)

if __name__ == "__main__":
  main()