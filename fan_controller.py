import time
import random
import sys

class FanController:
    def __init__(self, critical_temp=85, shutdown_temp=100):
        self.fan_speed = 0  # Fan initially off
        self.critical_temp = critical_temp
        self.shutdown_temp = shutdown_temp

    def get_current_temperature(self):
        # Simulate getting the system's temperature (random between 30 and 105)
        return random.uniform(30, 105)

    def set_fan_speed(self, temp):
        if temp < 40:
            self.fan_speed = 0  # Fan off
        elif 40 <= temp < 60:
            self.fan_speed = 1  # Fan low speed
        elif 60 <= temp < 80:
            self.fan_speed = 2  # Fan medium speed
        elif 80 <= temp < self.critical_temp:
            self.fan_speed = 3  # Fan high speed
        else:
            self.fan_speed = 4  # Critical temp: Fan max speed, emergency mode
        
        self.display_fan_status(temp)

    def display_fan_status(self, temp):
        speeds = ["OFF", "LOW", "MEDIUM", "HIGH", "MAX"]
        print(f"Current Temperature: {temp:.2f}°C | Fan Speed: {speeds[self.fan_speed]}")

        if temp >= self.critical_temp:
            print("WARNING: Critical Temperature! Fan at MAX speed.")

        if temp >= self.shutdown_temp:
            self.emergency_shutdown()

    def emergency_shutdown(self):
        print(f"Temperature has reached {self.shutdown_temp}°C!")
        print("EMERGENCY SHUTDOWN initiated. All processes halted, except fan.")
        print("Fan will run at MAX speed for 5 minutes to cool the system.")
        # Keep fan running at MAX for 5 minutes
        self.fan_speed = 4
        for i in range(5, 0, -1):
            print(f"Cooling down... Fan running for {i} more minute(s).")
            time.sleep(60)  # Simulate 1 minute of fan running
        print("System is now fully cooled. Shutting off the fan.")
        sys.exit("System shutdown complete. You can now restart your computer.")
    
    def monitor_system(self, duration=20):
        for _ in range(duration):
            current_temp = self.get_current_temperature()
            self.set_fan_speed(current_temp)
            if current_temp >= self.shutdown_temp:
                # If temperature hits shutdown temp, no further monitoring
                break
            time.sleep(1)  # Wait 1 second before next temperature check

if __name__ == "__main__":
    fan_controller = FanController()
    print("Monitoring system temperature and controlling fan speed...")
    fan_controller.monitor_system(30)  # Monitor for 30 seconds
