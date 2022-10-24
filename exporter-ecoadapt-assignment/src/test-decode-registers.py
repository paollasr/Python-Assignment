

from http import client
from unittest import skip
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
from pyModbusTCP.server import ModbusServer

ADDRESS = "127.0.0.1"

def run_sync_client():
    client = ModbusServer(ADDRESS, port=9000)
    client.connect()
    
# example write a float value using modscan data scanner
payload_builder = BinaryPayloadBuilder (byteorder=Endian.Big, wordorder= Endian.Big)
payload = payload_builder.add_32bit_float(99.898)
# rw = ModbusServer._write_single_register(1, payload) 


#example to read 16bit registers and return float using modsim data simulator
value_read = ModbusServer._read_words (0, 2) #address,count
decode_register = BinaryPayloadDecoder.fromRegisters(value_read.registers, byteorder=Endian.Big, wordorder= Endian.Big)

decoded_value = decode_register.decode_32bit_float()
print(value_read.registers)
print(decoded_value)