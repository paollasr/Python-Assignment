import paho.mqtt.client as paho
import sys

def on_message(client, userdata, msg):
    print(msg.topic + ":" + msg.payload.decoded())

client = paho.Client
client.on_message = on_message

client.connect("127.0.0.1", 1883, 100)
print("connecting to MQTT Broker")
    

# subscribing mqtt topic: Modbus
client.subscribe ("Modbus")

try:
    print("Ctrl+C to exit")
    client.loop_forever()
    
except:
    print("Disconnecting MQTT Broker")
    client.disconnect()