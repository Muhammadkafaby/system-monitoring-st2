import psutil
import requests
import yaml
import time

class NetworkMonitoringSensor:
    def __init__(self, discord_webhook_url, thresholds):
        self.discord_webhook_url = discord_webhook_url
        self.thresholds = thresholds

    def send_notification(self, message):
        requests.post(self.discord_webhook_url, json={"content": message})

    def monitor_network(self):
        while True:
            net_io = psutil.net_io_counters()
            sent_bytes = net_io.bytes_sent
            recv_bytes = net_io.bytes_recv

            if sent_bytes > self.thresholds['max_sent'] or recv_bytes > self.thresholds['max_received']:
                message = f"Alert: Network usage exceeded! Sent: {sent_bytes}, Received: {recv_bytes}"
                self.send_notification(message)

            time.sleep(self.thresholds['check_interval'])

if __name__ == "__main__":
    with open('config/discord.yaml') as f:
        discord_config = yaml.safe_load(f)
    
    with open('config/thresholds.yaml') as f:
        thresholds = yaml.safe_load(f)

    sensor = NetworkMonitoringSensor(discord_config['webhook_url'], thresholds['network'])
    sensor.monitor_network()