def set_thresholds(thresholds):
    """
    Set new resource usage thresholds via Discord commands.
    
    Args:
        thresholds (dict): A dictionary containing the new thresholds for CPU, RAM, disk, etc.
    """
    # Load current thresholds from configuration
    current_thresholds = load_current_thresholds()

    # Update thresholds with new values
    current_thresholds.update(thresholds)

    # Save updated thresholds back to configuration
    save_thresholds(current_thresholds)

    # Send confirmation notification to Discord
    send_discord_notification("Thresholds updated successfully.", current_thresholds)

def load_current_thresholds():
    # Logic to load current thresholds from config/thresholds.yaml
    pass

def save_thresholds(thresholds):
    # Logic to save updated thresholds to config/thresholds.yaml
    pass

def send_discord_notification(message, data):
    # Logic to send a notification to Discord
    pass