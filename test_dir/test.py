import ctypes
 
 
class my_struct(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('data_1', ctypes.c_int),
        ('data_2', ctypes.c_int8),
        ('data_3', ctypes.c_uint8),
    ]
 
 
print(ctypes.sizeof(my_struct))