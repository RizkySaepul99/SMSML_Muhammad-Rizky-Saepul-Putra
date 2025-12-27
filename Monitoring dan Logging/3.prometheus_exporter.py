from prometheus_client import Counter, Histogram, Gauge, start_http_server
import time
import psutil
import requests

REQUEST_COUNT = Counter(
    "ml_requests_total",
    "Total ML inference requests"
)

REQUEST_LATENCY = Histogram(
    "ml_request_latency_seconds",
    "Latency of ML inference requests"
)

MEMORY_USAGE = Gauge(
    "ml_memory_usage_mb",
    "Memory usage in MB"
)

def collect_metrics():
    while True:
        MEMORY_USAGE.set(psutil.virtual_memory().used / 1024 / 1024)
        time.sleep(5)

def simulate_inference():
    start = time.time()
    try:
        requests.get("http://localhost:9000")
        REQUEST_COUNT.inc()
    finally:
        REQUEST_LATENCY.observe(time.time() - start)

if __name__ == "__main__":
    start_http_server(8000)
    print("Exporter running on port 8000")

    while True:
        simulate_inference()
        collect_metrics()
