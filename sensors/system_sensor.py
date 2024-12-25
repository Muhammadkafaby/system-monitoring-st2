import psutil
import time
from st2reactor.sensor.base import Sensor

class SystemSensor(Sensor):
    def __init__(self, sensor_service, config=None):
        super(SystemSensor, self).__init__(sensor_service=sensor_service)
        self._config = config or {}
        self._thresholds = self._config.get('thresholds', {})
        self._running = True

    def setup(self):
        pass

    def run(self):
        while self._running:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent

            if cpu_usage > self._thresholds.get('cpu', 90):
                self._emit_event('cpu_usage_high', {'cpu_usage': cpu_usage})

            if memory_usage > self._thresholds.get('memory', 90):
                self._emit_event('memory_usage_high', {'memory_usage': memory_usage})

            time.sleep(5)

    def cleanup(self):
        self._running = False

    def _emit_event(self, event_type, payload):
        self.sensor_service.dispatch(event_type, payload)