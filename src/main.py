import json
import logging.handlers
import logging
import psycopg2
import datetime as dt
import os

from dotenv import load_dotenv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from src.mqttconnector import MqttProvider

def on_message(client, userdata, msg):

    try:
        topic = msg.topic
        payload = msg.payload.decode('utf-8')
        json_payload = json.loads(payload)
        timestamp = dt.datetime.fromisoformat(json_payload["received_at"])

        conn_string = f"host={DB_HOST} user={DB_USER} dbname=time_series_data password={DB_PASSWORD} sslmode=require"
        conn = psycopg2.connect(conn_string)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS mqtt_events (
            timestamp TIMESTAMP,
            topic TEXT,
            payload JSONB,
            PRIMARY KEY (timestamp, topic)
        );
        """
        cursor.execute(create_table_query)

        # Insert data into the table
        insert_query = "INSERT INTO mqtt_events (timestamp, topic, payload) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (timestamp, topic, payload))
        conn.commit()

    except Exception as e:
        print(f"ON_MESSAGE ERROR: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

##### START OF MAIN SCRIPT #####

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
logger = logging.getLogger()
for handler in logger.handlers:
    handler.setFormatter(formatter)

# MQTT Broker Configuration
MQTT_BROKER = os.environ.get("MQTT_BROKER", "")
MQTT_PORT = os.environ.get("MQTT_PORT", "1883") 
MQTT_TOPIC = os.environ.get("MQTT_TOPIC", "v3/+/devices/+/up")
MQTT_USERNAME = os.environ.get("MQTT_USERNAME", "")
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD", "")

# PostgreSQL Database Configuration
DB_HOST = os.environ.get("DB_HOST", "")
DB_NAME = os.environ.get("DB_NAME", "")
DB_USER = os.environ.get("DB_USER", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

mqtt_provider = MqttConnector(MQTT_BROKER, MQTT_USERNAME, MQTT_PASSWORD, MQTT_PORT)
mqtt_provider.subscribe(MQTT_TOPIC, on_message=on_message)
