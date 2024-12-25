import psutil
import requests
import yaml
from datetime import datetime

class ResourceMonitoringSensor:
    def __init__(self, discord_webhook_url, thresholds):
        self.discord_webhook_url = discord_webhook_url
        self.thresholds = thresholds

    def send_notification(self, message):
        payload = {"content": message}
        requests.post(self.discord_webhook_url, json=payload)

    def check_resources(self):
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        alerts = []

        if cpu_usage > self.thresholds['cpu']:
            alerts.append(f"High CPU usage detected: {cpu_usage}%")
        
        if ram_usage > self.thresholds['ram']:
            alerts.append(f"High RAM usage detected: {ram_usage}%")
        
        if disk_usage > self.thresholds['disk']:
            alerts.append(f"High Disk usage detected: {disk_usage}%")

        return alerts

    def run(self):
        alerts = self.check_resources()
        if alerts:
            for alert in alerts:
                self.send_notification(alert)

if __name__ == "__main__":
    with open('config/discord.yaml') as f:
        discord_config = yaml.safe_load(f)
    
    with open('config/thresholds.yaml') as f:
        thresholds = yaml.safe_load(f)

    sensor = ResourceMonitoringSensor(discord_config['webhook_url'], thresholds)
    sensor.run()