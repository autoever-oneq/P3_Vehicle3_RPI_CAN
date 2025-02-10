from can_message import *
from dataclasses import dataclass

@dataclass
class VehicleControlValues:
    steering_angle_delta: int
    motor1_rpm_delta: int
    motor2_rpm_delta: int

class CANMethod:
    
    # model에서 나온 값들 변경해서 전달..?
    def make_vehicle_control_values(self):
        return VehicleControlValues(steering_angle_delta=-30, motor1_rpm_delta=-3000, motor2_rpm_delta=-3511)
    
    def parse_vehicle_control_Message(self, values: VehicleControlValues):
        msg_struct = VehicleControlMsg()
        msg_struct.steering_angle_delta = values.steering_angle_delta & 0x7F  
        msg_struct.motor1_rpm_delta = values.motor1_rpm_delta & 0xFFFF
        msg_struct.motor2_rpm_delta = values.motor2_rpm_delta & 0xFFFF
        return bytes(msg_struct)
    

# -30 -3000 3511 >> 0000 0110 1101 1011 1111 1010 0010 0100 0110 0010 >> 6224fadb06000000
# -30  3000 3511 >> 0000 0110 1101 1011 1000 0101 1101 1100 0110 0010 >> 62dc85db06000000
# 30   3000 3511 >> 0000 0110 1101 1011 1000 0101 1101 1100 0001 1110 >> 