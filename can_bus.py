import can
from ctypes import *

class CANBus:
    def __init__(self):
        try:
            # PCAN-USB 설정
            self.bus = can.interface.Bus(
                channel='can0', 
                interface='socketcan',  
                bitrate=500000           # CAN 통신 속도 (500 kbit/s)
            )
            print("PCAN-USB initialized successfully")
        except can.CanError as e:
            print(f"Error initializing PCAN-USB: {e}")
            raise
    
    def stop_receiver(self):
        try:
            self.bus.shutdown()
            print("CAN receiver stopped")
        except Exception as e:
            print(f"Error stopping receiver: {e}")


    def send_message(self, msg_id, data):
        try:
            message = can.Message(
                arbitration_id=msg_id,
                data=data,
                is_extended_id=False
            )
            self.bus.send(message)
            print(f"Message sent - ID: 0x{msg_id:X}")
        except can.CanError as e:
            print(f"Error sending message: {e}")