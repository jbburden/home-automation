import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23,GPIO.OUT)
print "LED 1 on"
GPIO.output(23,GPIO.HIGH)
time.sleep(10)
print "LED 1 off"
GPIO.output(23,GPIO.LOW)

GPIO.setup(24,GPIO.OUT)
print "LED 2 on"
GPIO.output(24,GPIO.HIGH)
time.sleep(10)
print "LED 2 off"
GPIO.output(24,GPIO.LOW)
