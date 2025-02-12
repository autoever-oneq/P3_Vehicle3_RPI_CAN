from can_message import *
from can_info import *
from can_bus import *
from can_manager import *

import time

def main():
    can_manager = CANManager()
    can_manager.start()
    
    try:
        while True:
            current_status = can_manager.get_vehicle_status()
            print("Current Vehicle Status:", current_status)
            
            user_input = input("Send control message? (y/n): ")
            data = [float(x) if '.' in x else int(x) for x in user_input.split()]
            
            can_manager.send_msg(VEHICLE_CONTROL_ID,data)
            
    except KeyboardInterrupt:
        print("Stopping CANManager...")
    finally:
        can_manager.stop()
    

if __name__ == "__main__":
    main()