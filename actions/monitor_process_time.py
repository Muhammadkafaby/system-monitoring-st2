import psutil
import time
from st2common.runners.base_action import Action
from st2common.models.system.action import Action as St2Action

class MonitorProcessTimeAction(Action):
    def run(self, threshold):
        high_time_processes = []
        
        # Monitor processes
        for proc in psutil.process_iter(['pid', 'name', 'create_time']):
            try:
                # Calculate process execution time
                exec_time = time.time() - proc.info['create_time']
                
                # Check if execution time exceeds threshold
                if exec_time > threshold:
                    high_time_processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'execution_time': exec_time
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Notify if there are processes exceeding the threshold
        if high_time_processes:
            self.send_notification(high_time_processes)
        
        return high_time_processes

    def send_notification(self, high_time_processes):
        # Logic to send notification to Discord
        message = "Processes exceeding execution time threshold:\n"
        for proc in high_time_processes:
            message += f"PID: {proc['pid']}, Name: {proc['name']}, Execution Time: {proc['execution_time']:.2f} seconds\n"
        
        # Call the Discord notification action
        discord_action = St2Action('send_discord_notification')
        discord_action.run(message)