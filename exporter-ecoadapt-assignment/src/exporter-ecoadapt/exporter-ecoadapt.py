# !/usr/bin/env python3
"""
A minimal EcoAdapt modbus reader
"""

from atexit import register
import logging
import time
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
import paho.mqtt.client as mqtt
from pymodbus.compat import iteritems
import sys
import json


from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# configure the client logging
FORMAT = (
    "%(asctime)-15s %(threadName)-15s "
    "%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s"
)
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

UNIT = 0x1
ADDRESS = "127.0.0.1"
DATA = random.randint(1,100)

def run_sync_client():
    log.info("Setting up client")
    client = ModbusClient(ADDRESS, port=9000)
    client.connect()

    #RMS Voltage Registers 352-387
    #Frequency Registers 424-459
    log.info("Reading registers")
    read_registers = [
        (0, 1),
        (1, 1),
        (2, 3),
        (352, 12),
        (388, 12),
        (424, 12),
        (460, 12),
        
    ]
    
    mqttclient = mqtt.Client("Python Client")
    print("Connection to:", mqttclient)

    mqttclient.connect("127.0.0.1", 1883, 100)
    mqttclient.loop_start()
    
    for r in read_registers:
        resp = client.read_input_registers(r[0], r[1], unit=UNIT)
        #msg = log.info("%s: %s: %s" % (r, resp, resp.registers))
        #registers =json.dumps(resp.registers) # encode object to JSON
        data = bytearray(resp.registers) #check this
        mqttclient.publish ("Modbus", data, 0)
        print (r, resp.registers)

        # # using Binary Payload Decoder to register values
    # log.debug("Decoding input register values")
    # decoder = BinaryPayloadDecoder.fromRegisters(registers, endian=Endian.Big)
    # decoded = decoder.decode_32bit_float()
    # log.debug("Decoded values:")
    # for name, value in iteritems(decoded):
    #     print ("%s\t" % name, value)
    
        #publishing data periodically
    # while True:
    #    mqttclient.publish ("Modbus", data, 0)
    #    time.sleep(60)
    #    print (r, resp.registers)
    
        mqttclient.disconnect()
        
    log.info("Closing client")
    client.close()


if __name__ == "__main__":
    run_sync_client()

 


    

""""
Output when ran:
>> python3 ./src/exporter-ecoadapt/exporter-ecoadapt.py 
2021-03-19 12:31:18,597 MainThread      INFO     exporter-ecoadapt:23       Setting up client
2021-03-19 12:31:18,610 MainThread      INFO     exporter-ecoadapt:27       Reading registers
2021-03-19 12:31:18,615 MainThread      INFO     exporter-ecoadapt:39       (0, 1): ReadRegisterResponse (1): [514]
2021-03-19 12:31:18,622 MainThread      INFO     exporter-ecoadapt:39       (1, 1): ReadRegisterResponse (1): [2]
2021-03-19 12:31:18,635 MainThread      INFO     exporter-ecoadapt:39       (2, 3): ReadRegisterResponse (3): [30, 44285, 17639]
2021-03-19 12:31:18,643 MainThread      INFO     exporter-ecoadapt:39       (244, 12): ReadRegisterResponse (12): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
2021-03-19 12:31:18,646 MainThread      INFO     exporter-ecoadapt:39       (352, 12): ReadRegisterResponse (12): [49709, 17262, 20887, 15905, 45177, 15748, 0, 0, 0, 0, 0, 0]
2021-03-19 12:31:18,650 MainThread      INFO     exporter-ecoadapt:39       (388, 12): ReadRegisterResponse (12): [34030, 17262, 13400, 15907, 22707, 15748, 0, 0, 0, 0, 0, 0]
2021-03-19 12:31:18,654 MainThread      INFO     exporter-ecoadapt:39       (424, 12): ReadRegisterResponse (12): [54339, 16973, 54339, 16973, 43051, 16949, 0, 0, 0, 0, 0, 0]
2021-03-19 12:31:18,655 MainThread      INFO     exporter-ecoadapt:41       Closing client
"""