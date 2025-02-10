import can
import struct
from can_message import *


# vcan0에서 수신 대기
bus = can.interface.Bus(channel='can0', interface='socketcan')

try:
    while True:
        msg = bus.recv()  # CAN 메시지 수신
        
        if msg.arbitration_id == VEHICLE_STATUS_ID:
            print(f"receive CAN msg: ID={hex(msg.arbitration_id)}, data={msg.data}")
            
            msg_data = VehicleStatusMsg.from_buffer_copy(msg.data)
            
            print(msg_data)
            print(f"Motor1 RPM (raw): {msg_data.motor1_cur_rpm / 100.0}")
            print(f"Motor2 RPM (raw): {msg_data.motor2_cur_rpm / 100.0}")
        else:
            print("not receive")
        
except KeyboardInterrupt:
    print("Message sending stopped by user")
except can.CanError as e:
    print(f"CAN Error: {e}")