import logging

# Configure logging
logging.basicConfig(
    filename='system_actions.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_action(action_description):
    """
    Logs the action taken by the system.
    
    :param action_description: Description of the action to log
    """
    logging.info(action_description)

def log_error(error_description):
    """
    Logs an error encountered by the system.
    
    :param error_description: Description of the error to log
    """
    logging.error(error_description)

# Example usage
if __name__ == "__main__":
    log_action("Monitoring started.")
    log_error("Failed to detect zombie processes.")