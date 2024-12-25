import os
import subprocess
from st2common.runners.base_action import Action

class PowerSavingModeAction(Action):
    def run(self, action):
        if action == "activate":
            self.activate_power_saving_mode()
        elif action == "deactivate":
            self.deactivate_power_saving_mode()
        else:
            return "Invalid action. Use 'activate' or 'deactivate'."

    def activate_power_saving_mode(self):
        # Logic to activate power-saving mode
        subprocess.call(["systemctl", "set-default", "power-saving.target"])
        return "Power-saving mode activated."

    def deactivate_power_saving_mode(self):
        # Logic to deactivate power-saving mode
        subprocess.call(["systemctl", "set-default", "multi-user.target"])
        return "Power-saving mode deactivated."