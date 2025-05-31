import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pandas as pd
import logging
from prometheus_client import Gauge
import joblib
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Prometheus metrics
ANOMALY_SCORE = Gauge('anomaly_score', 'Anomaly detection score')
PREDICTION_CONFIDENCE = Gauge('prediction_confidence', 'Confidence of anomaly prediction')

class AnomalyDetector:
    def __init__(self):
        self.model_path = 'models/anomaly_detector.joblib'
        self.scaler_path = 'models/scaler.joblib'
        self.model = None
        self.scaler = None
        self.initialize_model()

    def initialize_model(self):
        """Initialize or load the anomaly detection model"""
        try:
            if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
                self.model = joblib.load(self.model_path)
                self.scaler = joblib.load(self.scaler_path)
                logger.info("Loaded existing anomaly detection model")
            else:
                self.model = IsolationForest(
                    contamination=0.1,
                    random_state=42,
                    n_estimators=100
                )
                self.scaler = StandardScaler()
                logger.info("Initialized new anomaly detection model")
        except Exception as e:
            logger.error(f"Error initializing model: {e}")
            raise

    def prepare_features(self, metrics):
        """Prepare features for anomaly detection"""
        features = np.array([
            metrics['cpu_usage'],
            metrics['memory_usage'],
            metrics['disk_usage']
        ]).reshape(1, -1)
        return self.scaler.transform(features)

    def detect_anomaly(self, metrics):
        """Detect anomalies in system metrics"""
        try:
            features = self.prepare_features(metrics)
            score = self.model.score_samples(features)[0]
            prediction = self.model.predict(features)[0]
            
            # Update Prometheus metrics
            ANOMALY_SCORE.set(score)
            PREDICTION_CONFIDENCE.set(abs(score))
            
            is_anomaly = prediction == -1
            logger.info(f"Anomaly detection - Score: {score:.2f}, Is Anomaly: {is_anomaly}")
            
            return {
                'is_anomaly': bool(is_anomaly),
                'score': float(score),
                'confidence': float(abs(score))
            }
        except Exception as e:
            logger.error(f"Error in anomaly detection: {e}")
            return None

    def train(self, historical_data):
        """Train the model with historical data"""
        try:
            # Convert historical data to DataFrame
            df = pd.DataFrame(historical_data)
            features = df[['cpu_usage', 'memory_usage', 'disk_usage']].values
            
            # Fit scaler and transform features
            self.scaler.fit(features)
            scaled_features = self.scaler.transform(features)
            
            # Train model
            self.model.fit(scaled_features)
            
            # Save model and scaler
            os.makedirs('models', exist_ok=True)
            joblib.dump(self.model, self.model_path)
            joblib.dump(self.scaler, self.scaler_path)
            
            logger.info("Successfully trained and saved anomaly detection model")
            return True
        except Exception as e:
            logger.error(f"Error training model: {e}")
            return False 