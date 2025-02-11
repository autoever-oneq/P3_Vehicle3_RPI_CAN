import threading

from can_message import *
from can_info import *
from can_bus import *
from vehicle_status import *

class CANManager:
    def __init__(self):
        self.can_bus = CANBus()
        self.can_method = CANMethod()
        self.vehicle_status = VehicleStatus()
        self.running = True
        
        self.receiver_thread = threading.Thread(target=self._receive_loop, daemon=True)
        # self.sender_thread = threading.Thread(target=self._send, daemon=True)
    
    def start(self):
        self.receiver_thread.start()
        # self.sender_thread.start()
        print("CANManager started.")
    
    def stop(self):
        self.running = False
        self.can_bus.stop_receiver()
        
    def _receive_loop(self):
        print("Starting CAN receive loop")
        while self.running:
            msg = self.can_bus.bus.recv()
            if msg.arbitration_id == VEHICLE_STATUS_ID:
                # print(f"Received CAN msg: ID={hex(msg.arbitration_id)}, data={msg.data}")
                try:
                    msg_data = VehicleStatusMsg.from_buffer_copy(msg.data)
                    motor1_rpm = msg_data.motor1_cur_rpm / 100.0
                    motor2_rpm = msg_data.motor2_cur_rpm / 100.0
                    
                    self.vehicle_status.update(motor1_rpm, motor2_rpm)
                except Exception as e:
                    print("Error parsing VehicleStatusMsg:", e)
            else:
                print(f"Received non-status message: ID={hex(msg.arbitration_id)}")
        
    def _send(self, data: list[int]):
        control_data = self.can_method.create_vehicle_control_data(data)
        data_to_send = self.can_method.encode_vehicle_control_Message(control_data)
        self.can_bus.send_message(VEHICLE_CONTROL_ID, data_to_send)
        
    def get_vehicle_status(self):
        return self.vehicle_status.get_status()