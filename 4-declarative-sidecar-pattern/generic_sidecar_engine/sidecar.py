import redis
import json
import time
import yaml
from collections import Counter


# --- METRIC ENGINE ---
# This part is generic and driven by the config.

class Metric:
    """Base class for all metric types."""

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def process(self, event):
        raise NotImplementedError

    def report(self):
        raise NotImplementedError


class CounterMetric(Metric):
    def __init__(self, name, config):
        super().__init__(name, config)
        self.count = 0

    def process(self, event):
        self.count += 1

    def report(self):
        return {"total": self.count}


class CategoricalCounterMetric(Metric):
    def __init__(self, name, config):
        super().__init__(name, config)
        self.field = config['field']
        self.counts = Counter()

    def process(self, event):
        if self.field in event:
            self.counts[event[self.field]] += 1

    def report(self):
        return dict(self.counts.most_common(5))


class AverageMetric(Metric):
    def __init__(self, name, config):
        super().__init__(name, config)
        self.field = config['field']
        self.total = 0
        self.count = 0

    def process(self, event):
        if self.field in event and isinstance(event[self.field], (int, float)):
            self.total += event[self.field]
            self.count += 1

    def report(self):
        avg = round(self.total / self.count, 2) if self.count > 0 else 0
        return {"average": avg, "count": self.count}


METRIC_TYPES = {
    'counter': CounterMetric,
    'categorical_counter': CategoricalCounterMetric,
    'average': AverageMetric,
}


def load_metrics_from_config(config_path):
    """Parses the YAML config and initializes metric objects."""
    print(f"🔩 Loading metric configuration from {config_path}...")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    metrics = []
    for m_config in config.get('metrics', []):
        m_type = m_config.get('type')
        m_name = m_config.get('name')
        if m_type in METRIC_TYPES:
            metrics.append(METRIC_TYPES[m_type](m_name, m_config))
            print(f"  -> Initialized metric '{m_name}' of type '{m_type}'")
    return metrics


# --- MAIN APPLICATION ---

def main():
    metrics = load_metrics_from_config("config.yaml")

    r = redis.Redis(host='redis', port=6379, db=0)
    p = r.pubsub()
    p.subscribe('events_channel')
    print("🚀 Sidecar subscribed to 'events_channel'. Waiting for messages...")

    last_report_time = time.time()
    while True:
        try:
            message = p.get_message()
            if message and message['type'] == 'message':
                event = json.loads(message['data'])
                # Process the event with all configured metrics
                for metric in metrics:
                    metric.process(event)

            if time.time() - last_report_time > 10:
                print("\n--- 📊 OBSERVABILITY REPORT ---")
                for metric in metrics:
                    print(f"  - {metric.name}: {metric.report()}")
                print("---------------------------------\n")
                last_report_time = time.time()

            time.sleep(0.01)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main()