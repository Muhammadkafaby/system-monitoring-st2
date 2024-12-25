# StackStorm Monitoring

This project is designed to monitor system metrics and send alerts to a Discord channel using StackStorm. It includes actions, sensors, and rules to facilitate monitoring and notification.

## Project Structure

- **actions/**: Contains action definitions for StackStorm.
  - `send_to_discord.yaml`: Action to send messages to a Discord webhook.

- **rules/**: Contains rules that define when actions should be triggered.
  - `monitor_rule.yaml`: Rule that triggers the Discord notification based on sensor data.

- **sensors/**: Contains sensor scripts that monitor system metrics.
  - `system_sensor.py`: Python script that monitors CPU and memory usage.

- **config/**: Contains configuration files for the monitoring system.
  - `config.yaml`: Configuration settings for sensors and actions.

- **pack.yaml**: Metadata for the StackStorm pack, including actions, sensors, and rules.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd stackstorm-monitoring
   ```

2. **Install StackStorm**
   Follow the [official StackStorm installation guide](https://docs.stackstorm.com/install/index.html) to set up StackStorm on your system.

3. **Configure the Monitoring System**
   Update the `config/config.yaml` file with any necessary parameters for your environment.

4. **Load the Pack**
   Use the StackStorm CLI to load the pack:
   ```bash
   st2 pack install .
   ```

5. **Start Monitoring**
   Ensure the sensor is running and the rules are active to start monitoring system metrics and sending notifications to Discord.

## Usage Examples

- The system will monitor CPU and memory usage. If usage exceeds predefined thresholds, a message will be sent to the specified Discord channel.

## Functionality

This monitoring system provides real-time insights into system performance and alerts users via Discord, ensuring timely responses to potential issues.