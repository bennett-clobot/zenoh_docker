# Some required imports
import zenoh
from pycdr import cdr
from pycdr.types import int8, int32, uint32, float64
import time

# Declare the types of Twist message to be encoded and published via zenoh
@cdr
class Vector3:
   x: float64
   y: float64
   z: float64

@cdr
class Twist:
   linear: Vector3
   angular: Vector3

# Declare the types of Log message to be decoded and subscribed to via zenoh
@cdr
class Time:
   sec: int32
   nanosec: uint32

@cdr
class Log:
   stamp: Time
   level: int8
   name: str
   msg: str
   file: str
   function: str
   line: uint32

@cdr
class Int32:
   data : int32

@cdr
class String:
   data : str

if __name__ == "__main__":
    session = zenoh.open({"mode":"peer"})
    while True:
       tmp = String(data="Hello world!").serialize()
       session.put('chatter',tmp)
       print("publish chatter")
    #time.sleep(60)
       time.sleep(1)