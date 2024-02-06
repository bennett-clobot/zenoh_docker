import zenoh
from pycdr import cdr
from pycdr.types import int8, int32, uint32, float64
import time

@cdr
class String:
   data : str

# Declare the callback and the subscriber for Log messages with key 'rt/rosout'
def rosout_callback(sample):
    result = String.deserialize(sample.payload)
    print('{}'.format(result.data))

if __name__ == "__main__":
    session = zenoh.open({"mode":"peer"})
    print(session)
    sub = session.declare_subscriber('chatter', rosout_callback)
    #time.sleep(60)
    time.sleep(1)