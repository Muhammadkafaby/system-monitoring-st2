# process_monitoring_sensor.py

import os
import time
import psutil
from st2common.runners.base_action import Action

class ProcessMonitoringSensor(Action):
    def run(self):
        while True:
            self.check_processes()
            time.sleep(60)  # Check every minute

    def check_processes(self):
        for proc in psutil.process_iter(['pid', 'name', 'status', 'create_time']):
            try:
                if proc.info['status'] == psutil.STATUS_ZOMBIE:
                    self.handle_zombie_process(proc)
                elif self.is_long_running_process(proc):
                    self.handle_long_running_process(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def handle_zombie_process(self, proc):
        # Logic to handle zombie process
        self.logger.info(f"Detected zombie process: {proc.info['name']} (PID: {proc.info['pid']})")
        # Trigger action to manage zombie process

    def is_long_running_process(self, proc):
        # Define a threshold for long-running processes (e.g., 300 seconds)
        return (time.time() - proc.info['create_time']) > 300

    def handle_long_running_process(self, proc):
        # Logic to handle long-running process
        self.logger.info(f"Detected long-running process: {proc.info['name']} (PID: {proc.info['pid']})")
        # Trigger action to notify or manage long-running process