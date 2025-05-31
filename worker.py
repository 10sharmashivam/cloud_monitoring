import time
import logging
import json
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ResourceMonitor:
    def __init__(self):
        self.metrics_file = 'metrics_history.json'
        self.initialize_metrics_file()

    def initialize_metrics_file(self):
        """Initialize metrics history file if it doesn't exist"""
        if not os.path.exists(self.metrics_file):
            with open(self.metrics_file, 'w') as f:
                json.dump([], f)

    def save_metrics(self, metrics):
        """Save metrics to history file"""
        try:
            with open(self.metrics_file, 'r') as f:
                history = json.load(f)
            
            history.append({
                'timestamp': datetime.now().isoformat(),
                'metrics': metrics
            })
            
            # Keep only last 1000 entries
            if len(history) > 1000:
                history = history[-1000:]
            
            with open(self.metrics_file, 'w') as f:
                json.dump(history, f)
            
            logger.info(f"Saved metrics for {datetime.now().isoformat()}")
        except Exception as e:
            logger.error(f"Error saving metrics: {e}")

    def process_metrics(self):
        """Process and analyze metrics"""
        while True:
            try:
                # Here you would typically:
                # 1. Collect metrics from your monitoring system
                # 2. Analyze trends
                # 3. Generate alerts if needed
                # 4. Store results
                
                sample_metrics = {
                    'cpu_usage': 45.5,
                    'memory_usage': 60.2,
                    'disk_usage': 75.8
                }
                
                self.save_metrics(sample_metrics)
                time.sleep(60)  # Process every minute
            except Exception as e:
                logger.error(f"Error processing metrics: {e}")
                time.sleep(5)

if __name__ == '__main__':
    monitor = ResourceMonitor()
    logger.info("Starting resource monitoring worker")
    monitor.process_metrics() 