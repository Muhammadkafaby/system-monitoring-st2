import psutil
import requests
import json
from config.discord import DISCORD_WEBHOOK_URL

def monitor_network():
    # Get network statistics
    net_io = psutil.net_io_counters()
    sent_bytes = net_io.bytes_sent
    recv_bytes = net_io.bytes_recv

    # Define thresholds (these can be customized)
    send_threshold = 1000000  # 1 MB
    recv_threshold = 1000000  # 1 MB

    # Check if the sent or received bytes exceed the thresholds
    if sent_bytes > send_threshold:
        alert_message = f"High network usage detected: Sent {sent_bytes} bytes."
        send_discord_notification(alert_message)

    if recv_bytes > recv_threshold:
        alert_message = f"High network usage detected: Received {recv_bytes} bytes."
        send_discord_notification(alert_message)

def send_discord_notification(message):
    payload = {
        "content": message
    }
    requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    monitor_network()