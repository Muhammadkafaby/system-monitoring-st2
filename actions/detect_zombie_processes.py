import os
import psutil
from st2common.runners.base_action import Action
from actions.send_discord_notification import send_discord_notification

class DetectZombieProcesses(Action):
    def run(self):
        zombie_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                if proc.info['status'] == psutil.STATUS_ZOMBIE:
                    zombie_processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        if zombie_processes:
            self.notify_discord(zombie_processes)
            return {"zombie_processes": zombie_processes}
        return {"message": "No zombie processes detected."}

    def notify_discord(self, zombie_processes):
        message = "Zombie Processes Detected:\n"
        for proc in zombie_processes:
            message += f"PID: {proc['pid']}, Name: {proc['name']}\n"
        send_discord_notification(message)