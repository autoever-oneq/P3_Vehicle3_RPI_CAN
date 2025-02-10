import can
import struct

# vcan0에서 수신 대기
bus = can.interface.Bus(channel='can0', interface='socketcan')

try:
    while True:
        msg = bus.recv()  # CAN 메시지 수신
        print(f"receive CAN msg: ID={hex(msg.arbitration_id)}, data={msg.data}")
        
        motor1_val, motor2_val = struct.unpack('<HH', msg.data[:4])
        print(f"Motor1 RPM (raw): {motor1_val / 100.0}")
        print(f"Motor2 RPM (raw): {motor2_val / 100.0}")
        
except KeyboardInterrupt:
    print("Message sending stopped by user")
except can.CanError as e:
    print(f"CAN Error: {e}")