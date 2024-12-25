import psutil
import json
import requests
from config.discord import DISCORD_WEBHOOK_URL
from config.thresholds import THRESHOLDS

def send_discord_notification(message):
    data = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

def monitor_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_io = psutil.net_io_counters()
    
    alerts = []

    if cpu_usage > THRESHOLDS['cpu']:
        alerts.append(f"High CPU usage detected: {cpu_usage}%")
    
    if ram_usage > THRESHOLDS['ram']:
        alerts.append(f"High RAM usage detected: {ram_usage}%")
    
    if disk_usage > THRESHOLDS['disk']:
        alerts.append(f"High Disk usage detected: {disk_usage}%")
    
    # Add network monitoring if needed
    # Example: if network_io.bytes_sent > THRESHOLDS['network']:
    #     alerts.append(f"High Network usage detected: {network_io.bytes_sent} bytes sent")

    if alerts:
        for alert in alerts:
            send_discord_notification(alert)

if __name__ == "__main__":
    monitor_resources()