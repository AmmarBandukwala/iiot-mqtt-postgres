# Local <dev> - Run from solution root.
# docker build -t mqtt-to-postgres:latest .
# docker run -it --rm --name my-python-container mqtt-to-postgres:latest /bin/bash
FROM python:3.11-slim

# ENVIORNMENT VARIABLES (Defaulting)
ENV MQTT_BROKER=""
ENV MQTT_PORT=""
ENV MQTT_TOPIC=""
ENV MQTT_USERNAME=""
ENV MQTT_PASSWORD=""

ENV DB_HOST=""
ENV DB_NAME=""
ENV DB_USER=""
ENV DB_PASSWORD=""

# Setup Python Pre-requisites and Run Script
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "src/main.py"]