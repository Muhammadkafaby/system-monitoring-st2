import requests
import yaml

def send_discord_notification(message):
    with open('config/discord.yaml') as config_file:
        config = yaml.safe_load(config_file)

    webhook_url = config['webhook_url']
    data = {
        "content": message
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code != 204:
        raise Exception(f"Failed to send notification: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
    send_discord_notification("This is a test notification from the StackStorm monitoring system.")