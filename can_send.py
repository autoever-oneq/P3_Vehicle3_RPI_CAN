import can
import struct
from can_message import *
from can_info import *
from can_bus import *


def main():
    try:
        can_bus = CANBus()
        can_method = CANMethod()
        vehicle_control_values = can_method.make_vehicle_control_values()
        
        data_bytes = can_method.parse_vehicle_control_Message(vehicle_control_values)
        print("Constructed data bytes:", data_bytes.hex())
        
        can_bus.send_message(VEHICLE_CONTROL_ID, data_bytes)
    finally:
        can_bus.stop_receiver()    

if __name__ == "__main__":
    main()