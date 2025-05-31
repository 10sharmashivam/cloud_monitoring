#!/bin/bash

# Install system dependencies
apt-get update
apt-get install -y python3-pip python3-dev build-essential

# Create and activate virtual environment
python3 -m venv /opt/venv
. /opt/venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run tests
pip install pytest pytest-cov
pytest --cov=./ --cov-report=xml

# Create necessary directories
mkdir -p /var/app/current/logs
mkdir -p /var/app/current/static

# Set permissions
chown -R webapp:webapp /var/app/current
chmod -R 755 /var/app/current 