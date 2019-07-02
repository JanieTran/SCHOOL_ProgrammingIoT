import paho.mqtt.publish as publish

MQTT_SERVER = "10.247.202.192"
MQTT_PATH = "test_channel"

publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
