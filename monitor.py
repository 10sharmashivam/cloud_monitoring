import time
import psutil
import logging
from prometheus_client import start_http_server, Gauge, Counter
from kubernetes import client, config
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Prometheus metrics
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU usage in percent')
MEMORY_USAGE = Gauge('memory_usage_percent', 'Memory usage in percent')
DISK_USAGE = Gauge('disk_usage_percent', 'Disk usage in percent')
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')

def get_kubernetes_metrics():
    """Get Kubernetes cluster metrics if running in a K8s environment"""
    try:
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        nodes = v1.list_node()
        pods = v1.list_pod_for_all_namespaces()
        
        logger.info(f"Kubernetes cluster has {len(nodes.items)} nodes and {len(pods.items)} pods")
        return True
    except Exception as e:
        logger.warning(f"Not running in Kubernetes environment: {e}")
        return False

def collect_metrics():
    """Collect system metrics"""
    while True:
        try:
            # System metrics
            CPU_USAGE.set(psutil.cpu_percent())
            MEMORY_USAGE.set(psutil.virtual_memory().percent)
            DISK_USAGE.set(psutil.disk_usage('/').percent)
            
            # Log metrics
            logger.info(f"CPU: {CPU_USAGE._value.get()}%")
            logger.info(f"Memory: {MEMORY_USAGE._value.get()}%")
            logger.info(f"Disk: {DISK_USAGE._value.get()}%")
            
            # Check Kubernetes if available
            get_kubernetes_metrics()
            
            time.sleep(15)  # Collect metrics every 15 seconds
        except Exception as e:
            logger.error(f"Error collecting metrics: {e}")
            time.sleep(5)

if __name__ == '__main__':
    # Start Prometheus metrics server
    start_http_server(8000)
    logger.info("Started metrics server on port 8000")
    
    # Start collecting metrics
    collect_metrics() 