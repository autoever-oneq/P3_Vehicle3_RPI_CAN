from can_message import *
from dataclasses import dataclass

@dataclass
class VehicleControlData:
    motor_rpm: float
    steering_angle_delta: int

class CANMethod:
    
    # model에서 나온 값들 변경해서 전달..?
    def create_vehicle_control_data(self, data_list: list) -> VehicleControlData:
        if len(data_list) != 2:
            raise ValueError("len 2")
        
        print("- CANMethod : create_vehicle_control_data")
        
        return VehicleControlData(motor_rpm=data_list[0], 
                                  steering_angle_delta=data_list[1], 
                                )
    
    def encode_vehicle_control_Message(self, values: VehicleControlData):
        print("- CANMethod : encode_vehicle_control_Message")
        msg_struct = VehicleControlMsg()
        msg_struct.steering_angle_delta = values.steering_angle_delta & 0x7F  
        msg_struct.motor_rpm = values.motor_rpm
        return bytes(msg_struct)
    

# -30 -3000 3511 >> 0000 0110 1101 1011 1111 1010 0010 0100 0110 0010 >> 6224fadb06000000
# -30  3000 3511 >> 0000 0110 1101 1011 1000 0101 1101 1100 0110 0010 >> 62dc85db06000000
# 30   3000 3511 >> 0000 0110 1101 1011 1000 0101 1101 1100 0001 1110 >> 