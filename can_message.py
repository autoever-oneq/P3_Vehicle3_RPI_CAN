from ctypes import *


# MSG_ID 
VEHICLE_CONTROL_ID =  0x200
VEHICLE_STATUS_ID = 0x100

class LogMsg(Structure):
    _pack_ = 1

    def __repr__(self):
        field_strings = []
        for field in self._fields_:
        
            field_name = field[0]
            field_value = getattr(self, field_name) 
            field_strings.append(f"{field_name}: {field_value}")
        return "\n".join(field_strings)
        
    
class VehicleStatusMsg(LogMsg):
    _fields_ = [
        ("motor1_cur_rpm", c_uint16, 16),  
        ("motor2_cur_rpm", c_uint16, 16) 
    ]

class VehicleControlMsg(LogMsg):
    _fields_ = [
        ("steering_angle_delta", c_int64, 7),  
        ("motor1_rpm_delta",     c_int64, 16),   
        ("motor2_rpm_delta",     c_int64, 16)    

    ]
    

