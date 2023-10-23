import RPi.GPIO as GPIO
import time

class Carwalk (object):

    def setup(self):
        GPIO.setmode(GPIO.BCM)

        #pins for motor A
        self.enableA = 18
        self.in1A = 23
        self.in2A = 24

        #pins for motor A
        self.enableB = 16
        self.in1B = 26
        self.in2B = 12

        #set up
        GPIO.setup(self.enableA, GPIO.OUT)
        GPIO.setup(self.enableB, GPIO.OUT)
        GPIO.setup(self.in1A, GPIO.OUT)
        GPIO.setup(self.in2A, GPIO.OUT)
        GPIO.setup(self.in1B, GPIO.OUT)
        GPIO.setup(self.in2B, GPIO.OUT)
        self.motorA_pwm = GPIO.PWM(self.enableA, 500)
        self.motorB_pwm = GPIO.PWM(self.enableB, 500)
        self.motorA_pwm.start(0)
        self.motorB_pwm.start(0)

        self.speed = 90
        self.tempoGiro = 1

    def forward (self):
        print("Going forward!!")
        # Motor A
        GPIO.output(self.in1A, False)
        GPIO.output(self.in2A, True)
        # Motor B
        GPIO.output(self.in1B, False)
        GPIO.output(self.in2B, True)
        # engine speed
        self.motorA_pwm.ChangeDutyCycle(self.speed)
        self.motorB_pwm.ChangeDutyCycle(self.speed)

    def right (self):
        print("Going right!!")
        # Motor A
        GPIO.output(self.in1A, False)
        GPIO.output(self.in2A, True)
        # motor B
        GPIO.output(self.in1B, False)
        GPIO.output(self.in2B, True)
        # engine speed
        self.motorA_pwm.ChangeDutyCycle(self.speed)
        self.motorB_pwm.ChangeDutyCycle(self.speed)
        time.sleep(self.tempoGiro)

    def left (self):
        print("Going left!!")
        # motor A
        GPIO.output(self.in1A, False)
        GPIO.output(self.in2A, True)
        # motor B
        GPIO.output(self.in1B, False)
        GPIO.output(self.in2B, True)
        # engine speed
        self.motorA_pwm.ChangeDutyCycle(self.speed)
        self.motorB_pwm.ChangeDutyCycle(self.speed)
        time.sleep(self.tempoGiro)

    def back (self):
        print("Reversing!!")
        # motor A
        GPIO.output(self.in1A, True)
        GPIO.output(self.in2A, False)
        # motor B
        GPIO.output(self.in1B, True)
        GPIO.output(self.in2B, False)
        # engine speed
        self.motorA_pwm.ChangeDutyCycle(self.speed)
        self.motorB_pwm.ChangeDutyCycle(self.speed)
        time.sleep(1)

    def stop (self):
        print("Stopping!!")
        # motor A
        GPIO.output(self.in1A, False)
        GPIO.output(self.in2A, False)
        # motor B
        GPIO.output(self.in1B, False)
        GPIO.output(self.in2B, False)
        # engine speed
        self.motorA_pwm.ChangeDutyCycle(0)
        self.motorB_pwm.ChangeDutyCycle(0)