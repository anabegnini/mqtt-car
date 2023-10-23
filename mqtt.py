# coding: utf-8

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from unicodedata import normalize
from carwalk import Carwalk
import time

Broker = "test.mosquitto.org"
topic = "/mqtt/ride/robot/publish/"
topic_subs = "mqtt/ride/robot/listener/"
PortaBroker = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected!")
    client.subscribe(topic_subs)
 
#Callback - mensage received from broker
def on_message(client, userdata, msg):

    Msg = str(msg.payload.decode("utf-8"))
    Msg = normalize('NFKD', Msg).encode('ASCII', 'ignore').decode('ASCII')

    print(f"Moving the robot:: {Msg}") 
    
    if Msg == "forward":
        robot.forward()
    elif Msg == "stop":
        robot.stop()
    elif Msg == "right":
        robot.right()
    elif Msg == "left":
        robot.left()
    elif Msg == "back":
        robot.back()

def mqtt_client_connect():
    print("Connecting to Broker...")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(Broker, PortaBroker)
    client.loop_start()

robot = Carwalk()
client = mqtt.Client("RPi")
mqtt_client_connect()

try:
  while True:
        client.publish(topic, "hello")
        time.sleep(2)
   
finally:
  GPIO.cleanup()
