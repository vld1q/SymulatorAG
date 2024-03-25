import turtle, serial, time, math
from maps import default
from config import app
serial_id = app["COM"]
map_defs = default.init()

if serial_id is not None: # use real hardware
    com = serial.Serial(f"COM{serial_id}")
    while(True):
        byte: chr = chr(default.render(*map_defs))
        com.write(f"{byte}".encode())
        val: int = int.from_bytes(com.read(1), byteorder="big")
        map_defs[0].right((float(val)/256.0)*90.0)
else:
    turtle.done()