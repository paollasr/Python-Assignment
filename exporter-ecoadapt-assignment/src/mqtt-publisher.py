import paho.mqtt.client as mqtt
import sys
import time

# mqtt call back methods

def on_log(client, userdata, level, buf):
    print("log: " + buf)
    
def on_connect(client, userdata, flags, rc):
    if rc ==0 : 
        print("[Connection]: CONNECTION OK")
    else:
        print("[Connection]: NOT OK", rc)
    
# instanciating a client

client = mqtt.Client("Python Client")
print("Connection to:", client)

client.on_log = on_log
client.on_connect = on_connect

if client.connect("127.0.0.1", 1883, 100) != 0:
    print("Not able to connect to MQTT Broker")
    
    sys.exit(-1)

# publiching test payload
client.publish ("Modbus", "Voltage: 230 V", 0)

client.disconnect()