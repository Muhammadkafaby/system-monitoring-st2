# StackStorm Monitoring System

This project implements a comprehensive monitoring and management system using StackStorm and Discord for real-time notifications and actions. The system is designed to enhance resource management, process monitoring, and automated recovery in a server environment.

## Features

- **Zombie Process Detection and Management**: Automatically identifies and manages zombie processes with validation through Discord notifications.
- **Real-Time Notifications**: Sends critical alerts for high CPU usage, disk space issues, and other important events directly to Discord.
- **Detailed Logging**: Logs all actions taken by the system, including process management and resource monitoring.
- **Resource Monitoring**: Monitors CPU, RAM, disk usage, and network activity, providing alerts based on customizable thresholds.
- **Temporary File Management**: Manages temporary files with notifications for deletion and confirmation through Discord.
- **Automated Reporting**: Generates daily and monthly reports on resource usage and optimization actions.
- **Dynamic Process Priority Management**: Adjusts process priorities based on resource usage and administrator commands.
- **Network Management**: Monitors network bandwidth and detects high usage processes, sending alerts as necessary.
- **Automatic Recovery**: Restarts failed services or containers automatically and notifies administrators.
- **Integration with External Monitoring**: Integrates with external monitoring systems and sends notifications to Discord.
- **Advanced Cache Cleaning**: Provides commands for cleaning specific caches and logs the results.
- **CPU Limitation**: Allows administrators to set CPU limits for specific processes.
- **Process Time Monitoring**: Monitors processes that exceed normal execution time and notifies administrators.
- **Multithreading Optimization**: Analyzes thread usage and provides optimization recommendations.
- **Customizable Thresholds**: Administrators can set new resource usage thresholds via Discord commands.
- **Power Saving Mode**: Activates or deactivates power-saving mode based on system status.
- **Malware Detection**: Scans for suspicious processes and notifies administrators of detected threats.
- **Docker Restart Automation**: Automatically restarts Docker containers that fail and notifies administrators.
- **Anomaly Detection**: Detects abnormal activities in the system and alerts administrators.
- **Self-Healing System**: Automatically fixes simple issues and reports the results.
- **Energy Efficiency Metrics**: Monitors energy efficiency and recommends power-saving measures.

## Setup Instructions

1. Clone the repository:

   ```
   git clone https://github.com/Muhammadkafaby/system-monitoring-st2.git
   ```

2. Navigate to the project directory:

   ```
   cd stackstorm-monitoring-system
   ```

3. Install the required dependencies for StackStorm and any additional libraries needed for Discord integration.

4. Configure the `config/discord.yaml` file with your Discord bot token and channel information.

5. Set up the necessary rules and actions in StackStorm using the provided YAML files in the `rules` and `actions` directories.

6. Start the StackStorm services and ensure that the sensors are running to monitor the system.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
