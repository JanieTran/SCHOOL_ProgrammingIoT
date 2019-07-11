import paho.mqtt.publish as publish
from sense_hat import SenseHat
from time import sleep

MQTT_SERVER = "10.247.202.192"
MQTT_PATH = "lab_test_2"


sense = SenseHat()

while True:
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    message = 'Temperature: {:.2f} deg C - Humidity: {:.2f}% - Pressure: {:.2f} atm'

    publish.single(MQTT_PATH, message.format(temperature, humidity, pressure), hostname=MQTT_SERVER)

    sleep(2)
