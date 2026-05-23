import time


class LatencyTracker:

    def __init__(self):

        self.metrics = {}

    def start(self, key):

        self.metrics[key] = {
            "start": time.perf_counter()
        }

    def stop(self, key):

        end_time = time.perf_counter()

        self.metrics[key]["end"] = end_time

        self.metrics[key]["duration_ms"] = round(
            (
                end_time -
                self.metrics[key]["start"]
            ) * 1000,
            2
        )

    def report(self):

        return {
            key: value["duration_ms"]
            for key, value in self.metrics.items()
        }