
from pyModbusTCP.server import ModbusServer

ip = "127.0.0.1"
port = 9000

#creating server instance
server = ModbusServer(ip, port, no_block=True)

try:
    print("Starting server on: " + ip )
    server.start()
    print("Server online!")
    
    while True:
        continue 
except:
    server.stop()
    print("Server offline" )


    