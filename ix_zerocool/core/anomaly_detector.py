"""
IX-ZeroCool Anomaly Detector

Analyzes incoming packet data and system activity logs for abnormal patterns.
Supports basic statistical deviation detection and pattern flagging.
"""

from typing import List, Dict
import statistics

class AnomalyDetector:
    def __init__(self):
        self.packet_sizes: List[int] = []
        self.threshold_multiplier = 2.5  # configurable sensitivity

    def log_packet_size(self, size: int):
        self.packet_sizes.append(size)

    def detect_anomaly(self) -> Dict[str, bool]:
        if len(self.packet_sizes) < 5:
            return {"anomaly": False, "reason": "Insufficient data"}

        mean = statistics.mean(self.packet_sizes)
        stdev = statistics.stdev(self.packet_sizes)
        latest = self.packet_sizes[-1]

        if abs(latest - mean) > self.threshold_multiplier * stdev:
            return {"anomaly": True, "reason": "Statistical deviation"}
        else:
            return {"anomaly": False, "reason": "Within expected range"}

# Example usage
if __name__ == "__main__":
    detector = AnomalyDetector()
    sizes = [512, 520, 518, 530, 1024]  # simulate packet sizes
    for size in sizes:
        detector.log_packet_size(size)
        result = detector.detect_anomaly()
        print(f"Packet size: {size} -> {result}")
