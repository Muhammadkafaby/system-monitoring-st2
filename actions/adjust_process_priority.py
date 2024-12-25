import os
import psutil
from st2common.runners.base_action import Action

class AdjustProcessPriorityAction(Action):
    def run(self, pid, priority):
        try:
            process = psutil.Process(pid)
            process.nice(priority)
            return f"Successfully adjusted priority of process {pid} to {priority}."
        except psutil.NoSuchProcess:
            return f"Process {pid} does not exist."
        except psutil.AccessDenied:
            return f"Access denied to adjust priority of process {pid}."
        except Exception as e:
            return str(e)