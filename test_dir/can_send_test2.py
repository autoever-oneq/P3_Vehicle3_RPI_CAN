import can
import struct
from can_message import *

# 데이터 생성
motor1_val = 5012  # 0x1394
motor2_val = 5143  # 0x1417

# 데이터 합치기 (리틀 엔디안)
data_bytes = struct.pack('<HH', motor1_val, motor2_val)  # 4바이트로 변환

# 나머지 4바이트는 0으로 채움
data_bytes += b'\x00\x00\x00\x00'  # 총 8바이트

# CAN 메시지 생성
msg = can.Message(
    arbitration_id=VEHICLE_STATUS_ID,  # 메시지 ID
    data=data_bytes,       # 8바이트 데이터
    is_extended_id=False   # 표준 CAN ID 사용
)

# CAN 메시지 전송
with can.Bus(channel='can0', interface='socketcan') as bus:
    try:
        print(f"data_bytes:{data_bytes}")
        bus.send(msg)
        print("CAN send success:", msg)
    except can.CanError:
        print("CAN send fail")
