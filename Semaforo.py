import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

def semaforo():
        print "Iniciando semaforo..."
        GPIO.output(4, True)
        time.sleep(5)

        GPIO.output(27, True)
        GPIO.output(4, False)
        time.sleep(5)

        GPIO.output(17,True)
        time.sleep(2)

        GPIO.output(17, False)
        GPIO.output(27, False)

GPIO.cleanip()