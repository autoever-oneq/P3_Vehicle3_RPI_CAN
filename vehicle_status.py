
import threading

class VehicleStatus:
    def __init__(self):
        self._lock = threading.Lock()
        self.motor_cur_rpm = 0.0

    def update(self, motor_rpm: float):
        with self._lock:
            self.motor_cur_rpm = round(motor_rpm, 3)

    def get_status(self):
        with self._lock:
            return {
                "motor_cur_rpm": self.motor_cur_rpm
            }