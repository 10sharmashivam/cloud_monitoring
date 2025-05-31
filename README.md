# Cloud Native Resource Monitoring Python App on Kubernetes 

This project is a Python-based cloud-native application designed to monitor system resources such as CPU and memory usage. The application uses Flask for the backend and Plotly for creating interactive gauge visualizations. It is containerized using Docker and can be deployed to Kubernetes for scalable and resilient deployment.

## 🌟 Features

- **Cloud-Agnostic Design**: Works seamlessly across AWS, GCP, and other cloud providers
- **Real-time Resource Monitoring**: CPU, Memory, and Disk usage tracking
- **Kubernetes Integration**: Native support for container orchestration
- **Prometheus Metrics**: Production-ready monitoring and alerting
- **CI/CD Pipeline**: Automated testing and deployment
- **Infrastructure as Code**: Cloud-agnostic deployment configurations
- **High Availability**: Designed for production workloads
- **Scalable Architecture**: Worker-based design for handling large workloads
- **ML-Powered Anomaly Detection**: Real-time anomaly detection using machine learning
- **Service Mesh Integration**: Istio-based traffic management and security

## 🛠️ Technology Stack

- **Backend**: Python 3.9
- **Web Framework**: Flask
- **Process Management**: Gunicorn
- **Containerization**: Docker
- **Monitoring**: Prometheus, Grafana
- **CI/CD**: GitHub Actions, Cloud Build
- **Cloud Platforms**: AWS, GCP (cloud-agnostic design)
- **Container Orchestration**: Kubernetes
- **Service Mesh**: Istio
- **Machine Learning**: scikit-learn, TensorFlow
- **Data Processing**: pandas, numpy

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker
- Kubernetes cluster (optional)
- Cloud provider account (AWS/GCP)
- Istio (for service mesh features)

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/10sharmashivam/cloud_monitoring.git
   cd cloud_native_resource_monitoring
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

### Docker Deployment

```bash
docker build -t cloud-monitoring .
docker run -p 5000:5000 cloud-monitoring
```

### Kubernetes with Istio Deployment

1. Install Istio:
   ```bash
   istioctl install -f istio/service-mesh.yaml
   ```

2. Deploy the application:
   ```bash
   kubectl apply -f k8s/
   kubectl apply -f istio/
   ```

## 📊 Monitoring

The system exposes Prometheus metrics at `/metrics` endpoint. Key metrics include:

- CPU Usage
- Memory Usage
- Disk Usage
- HTTP Request Count
- Kubernetes Cluster Metrics
- ML Anomaly Detection Scores
- Service Mesh Metrics

## 🤖 Machine Learning Features

- **Anomaly Detection**: Real-time detection of system anomalies using Isolation Forest
- **Predictive Analytics**: Resource usage forecasting
- **Automated Scaling**: ML-based scaling decisions
- **Model Management**: Automated model training and versioning

## 🔄 CI/CD Pipeline

The project includes:

- Automated testing with pytest
- Code coverage reporting
- Docker image building and pushing
- Cloud-agnostic deployment configurations
- Infrastructure as Code templates
- ML model training pipeline

## 🏗️ Infrastructure

### AWS Deployment
- Elastic Beanstalk configuration
- ECS/EKS support
- CloudWatch integration
- SageMaker integration for ML

### GCP Deployment
- Cloud Run configuration
- GKE support
- Cloud Monitoring integration
- Vertex AI integration for ML

## 🔐 Security

- Non-root container user
- Secure environment variables
- Regular security updates
- Cloud provider IAM integration
- Service mesh security policies
- ML model security

## 📈 Production Features

- Horizontal scaling support
- Load balancing
- Health checks
- Automated backups
- Log aggregation
- Alert management
- Service mesh traffic management
- ML model monitoring
