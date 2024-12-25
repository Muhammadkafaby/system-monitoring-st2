import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_cache(cache_type):
    """
    Cleans the specified cache type and logs the result.
    :param cache_type: Type of cache to clean (e.g., 'temp', 'apt', 'docker').
    """
    try:
        if cache_type == 'temp':
            os.system('rm -rf /tmp/*')
            logging.info("Temporary cache cleaned.")
        elif cache_type == 'apt':
            os.system('apt-get clean')
            logging.info("APT cache cleaned.")
        elif cache_type == 'docker':
            os.system('docker system prune -f')
            logging.info("Docker cache cleaned.")
        else:
            logging.warning("Unknown cache type specified.")
            return "Unknown cache type specified."
        
        return f"{cache_type.capitalize()} cache cleaned successfully."
    
    except Exception as e:
        logging.error(f"Error cleaning cache: {e}")
        return f"Error cleaning cache: {e}"

if __name__ == "__main__":
    # Example usage
    print(clean_cache('temp'))  # Change 'temp' to 'apt' or 'docker' as needed.