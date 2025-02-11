
import threading

class VehicleStatus:
    def __init__(self):
        self._lock = threading.Lock()
        self.motor1_cur_rpm = 0.0
        self.motor2_cur_rpm = 0.0

    def update(self, motor1_rpm: float, motor2_rpm: float):
        with self._lock:
            self.motor1_cur_rpm = motor1_rpm
            self.motor2_cur_rpm = motor2_rpm

    def get_status(self):
        with self._lock:
            return {
                "motor1_cur_rpm": self.motor1_cur_rpm,
                "motor2_cur_rpm": self.motor2_cur_rpm
            }