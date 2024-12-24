import os
import psutil
from st2reactor.sensor.base import Sensor

class ResourceMonitoringSensor(Sensor):
    def __init__(self, sensor_service, config=None):
        super(ResourceMonitoringSensor, self).__init__(sensor_service=sensor_service, config=config)
        self.thresholds = {
            'cpu': 90,
            'ram': 90,
            'disk': 90
        }

    def setup(self):
        self.logger.info("Resource Monitoring Sensor initialized.")

    def run(self):
        self.monitor_resources()

    def monitor_resources(self):
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        if cpu_usage > self.thresholds['cpu']:
            self.trigger_action('monitor_resources', {'type': 'cpu', 'usage': cpu_usage})

        if ram_usage > self.thresholds['ram']:
            self.trigger_action('monitor_resources', {'type': 'ram', 'usage': ram_usage})

        if disk_usage > self.thresholds['disk']:
            self.trigger_action('monitor_resources', {'type': 'disk', 'usage': disk_usage})

    def trigger_action(self, action, payload):
        self.sensor_service.dispatch_trigger(action, payload)

    def cleanup(self):
        self.logger.info("Resource Monitoring Sensor cleaned up.")