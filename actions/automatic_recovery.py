import subprocess
import logging
from send_discord_notification import send_notification

logging.basicConfig(level=logging.INFO)

def restart_service(service_name):
    try:
        subprocess.run(['systemctl', 'restart', service_name], check=True)
        logging.info(f"Successfully restarted service: {service_name}")
        send_notification(f"Service {service_name} has been restarted.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart service: {service_name}. Error: {e}")
        send_notification(f"Failed to restart service {service_name}. Error: {e}")

def check_and_restart_services(services):
    for service in services:
        status = subprocess.run(['systemctl', 'is-active', service], capture_output=True, text=True)
        if status.stdout.strip() != 'active':
            logging.warning(f"Service {service} is not active. Attempting to restart.")
            restart_service(service)

if __name__ == "__main__":
    services_to_monitor = ['your_service_name_1', 'your_service_name_2']  # Replace with actual service names
    check_and_restart_services(services_to_monitor)