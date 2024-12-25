import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def self_heal():
    # Example of simple self-healing actions
    try:
        # Check for common issues and attempt to fix them
        logging.info("Starting self-healing process...")

        # Restart a failed service (example: nginx)
        service_name = "nginx"
        result = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)

        if result.stdout.strip() != "active":
            logging.info(f"{service_name} is not running. Attempting to restart...")
            subprocess.run(["systemctl", "restart", service_name])
            logging.info(f"{service_name} has been restarted.")
        else:
            logging.info(f"{service_name} is running normally.")

        # Clean up temporary files (example path)
        temp_dir = "/tmp/my_temp_files"
        if os.path.exists(temp_dir):
            logging.info(f"Cleaning up temporary files in {temp_dir}...")
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                try:
                    os.remove(file_path)
                    logging.info(f"Removed {file_path}.")
                except Exception as e:
                    logging.error(f"Error removing {file_path}: {e}")

        logging.info("Self-healing process completed.")

    except Exception as e:
        logging.error(f"Self-heal process encountered an error: {e}")

if __name__ == "__main__":
    self_heal()