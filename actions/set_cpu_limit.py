import subprocess
import json
import requests

DISCORD_WEBHOOK_URL = "your_discord_webhook_url"

def set_cpu_limit(process_name, cpu_limit):
    try:
        # Find the process ID(s) by name
        result = subprocess.run(['pgrep', process_name], stdout=subprocess.PIPE, text=True)
        pids = result.stdout.strip().split('\n')

        if not pids or pids[0] == '':
            return {"status": "error", "message": "Process not found."}

        # Set CPU limit for each process
        for pid in pids:
            subprocess.run(['cpulimit', '-p', pid, '-l', str(cpu_limit)])

        # Send notification to Discord
        message = f"CPU limit set to {cpu_limit}% for process(es): {', '.join(pids)}"
        send_discord_notification(message)

        return {"status": "success", "message": message}

    except Exception as e:
        return {"status": "error", "message": str(e)}

def send_discord_notification(message):
    data = {
        "content": message
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data)

if __name__ == "__main__":
    # Example usage
    process_name = "example_process"
    cpu_limit = 50
    result = set_cpu_limit(process_name, cpu_limit)
    print(result)