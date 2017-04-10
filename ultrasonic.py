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

  # d = Ultrasonic(23, 24)

  TRIG = 23  # Associate pin 23 to TRIG
  ECHO = 24  # Associate pin 24 to ECHO

  print "Distance measurement in progress"

  GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out
  GPIO.setup(ECHO, GPIO.IN)  # Set pin as GPIO in

  while True:

    GPIO.output(TRIG, False)  # Set TRIG as LOW
    print "Waitng For Sensor To Settle"
    time.sleep(2)  # Delay of 2 seconds

    GPIO.output(TRIG, True)  # Set TRIG as HIGH
    time.sleep(0.00001)  # Delay of 0.00001 seconds
    GPIO.output(TRIG, False)  # Set TRIG as LOW

    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
      pulse_start = time.time()  # Saves the last known time of LOW pulse

    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
      pulse_end = time.time()  # Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable

    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)  # Round to two decimal points

    if distance > 2 and distance < 400:  # Check whether the distance is within range
      print "Distance:", distance - 0.5, "cm"  # Print distance with 0.5 cm calibration
    else:
      print "Out Of Range"  # display out of range

if __name__ == "__main__":
  main()