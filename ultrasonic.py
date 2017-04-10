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
    GPIO.output(self.trig, False)
    time.sleep(2)

    GPIO.output(self.trig, True)
    time.sleep(waitTime)
    GPIO.output(self.trig, False)

    while GPIO.input(self.echo) == 0:
      pulse_start = time.time()

    while GPIO.input(self.trig) == 1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    if distance > 2 and distance < 400:
      print "Distance:",distance - 0.5,"cm"
    else:
      print "Out Of Range"

    return distance


def main():
  print "hi"

  d = Ultrasonic(23, 24)

  while True:
    d.getDistance()
    time.sleep(1)

if __name__ == "__main__":
  main()