import subprocess
import logging
from send_discord_notification import send_notification

def restart_docker_container(container_name):
    try:
        # Restart the specified Docker container
        subprocess.run(["docker", "restart", container_name], check=True)
        logging.info(f"Successfully restarted Docker container: {container_name}")
        send_notification(f"Successfully restarted Docker container: {container_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart Docker container: {container_name}. Error: {e}")
        send_notification(f"Failed to restart Docker container: {container_name}. Error: {e}")

if __name__ == "__main__":
    # Example usage
    container_name = "your_container_name"  # Replace with your container name
    restart_docker_container(container_name)