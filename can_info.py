from can_message import *
from dataclasses import dataclass

@dataclass
class VehicleControlData:
    steering_angle_delta: int
    motor1_rpm_delta: int
    motor2_rpm_delta: int

class CANMethod:
    
    # model에서 나온 값들 변경해서 전달..?
    def create_vehicle_control_data(self, data_list: list[int]) -> VehicleControlData:
        if len(data_list) != 3:
            raise ValueError("len 3")
        
        
        return VehicleControlData(steering_angle_delta=data_list[0], 
                                    motor1_rpm_delta=data_list[1], 
                                    motor2_rpm_delta=data_list[2])
    
    def encode_vehicle_control_Message(self, values: VehicleControlData):
        msg_struct = VehicleControlMsg()
        msg_struct.steering_angle_delta = values.steering_angle_delta & 0x7F  
        msg_struct.motor1_rpm_delta = values.motor1_rpm_delta & 0xFFFF
        msg_struct.motor2_rpm_delta = values.motor2_rpm_delta & 0xFFFF
        return bytes(msg_struct)
    

# -30 -3000 3511 >> 0000 0110 1101 1011 1111 1010 0010 0100 0110 0010 >> 6224fadb06000000
# -30  3000 3511 >> 0000 0110 1101 1011 1000 0101 1101 1100 0110 0010 >> 62dc85db06000000
# 30   3000 3511 >> 0000 0110 1101 1011 1000 0101 1101 1100 0001 1110 >> 