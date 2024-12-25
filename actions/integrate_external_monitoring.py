import requests
import json
import logging

# Load Discord configuration
with open('../config/discord.yaml') as f:
    discord_config = yaml.safe_load(f)

DISCORD_WEBHOOK_URL = discord_config['webhook_url']

def send_discord_notification(message):
    payload = {
        "content": message
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    if response.status_code != 204:
        logging.error(f"Failed to send notification: {response.status_code} - {response.text}")

def integrate_with_external_monitoring(system_data):
    # Example integration logic with an external monitoring system
    try:
        # Send system data to external monitoring API
        external_api_url = "https://external-monitoring-system/api/data"
        response = requests.post(external_api_url, json=system_data)
        
        if response.status_code == 200:
            send_discord_notification("Successfully integrated with external monitoring system.")
        else:
            send_discord_notification(f"Failed to integrate with external monitoring system: {response.status_code}")
    except Exception as e:
        logging.error(f"Error integrating with external monitoring: {str(e)}")
        send_discord_notification(f"Error integrating with external monitoring: {str(e)}")

# Example usage
if __name__ == "__main__":
    system_data = {
        "cpu_usage": 75,
        "ram_usage": 60,
        "disk_usage": 80,
        "network_activity": 120
    }
    integrate_with_external_monitoring(system_data)