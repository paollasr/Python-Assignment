# test register address calculation

from enum import Enum
 
class Connector(Enum):
    SINGLEPHASE = 1
    THREEPHASEN = 2
    BALANCETHREEPHASEN = 3
    THREEPHASE = 4
    BALANCETHREEPHASE = 5
    THREEPAHSEVT = 6
    
class Channel(Enum):
    CH1 = 1
    CH2 = 2
    CH3 = 3

# initializing values to calculate register number
start = 424
n = Connector.THREEPAHSEVT.value
m = Channel.CH3.value

# calculating registe number
register_number = start + ((n-1)*3 + m -1) * 2

print(register_number)