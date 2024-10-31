import logging

from paho.mqtt import client as mqtt

class MqttConnector:

    def __init__(self)-> None:
        pass

    def __init__(self, host: str,  user: str, password: str, port: int = 8883) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.client: mqtt.Client = mqtt.Client()  
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.username_pw_set(username=self.user, password=self.password)
        self.client.tls_set()

    def publish(self, topic: str, payload, on_publish: tuple[()] = None):     
        try:                 
            self.client.on_publish = on_publish
            if self.client.is_connected() == False:
                self.client.connect(self.host, port=self.port)
            result = self.client.publish(topic=topic, payload=payload)
            status = result[0]
            if status == 0:
                logging.info(f"MQTT CLIENT - Publish - Send `{payload}` to topic `{topic}`")
            else:
                logging.error(f"MQTT CLIENT - Publish - Failed to send message to topic {topic} error code {status}.")
        except Exception as e:
            logging.exception(f"MQTT CLIENT - Publish - Error - {e.args[0]}")

    def subscribe(self, mqtt_topic: str, on_message: function):
        self.client.on_message = on_message
        self.client.connect(self.host, self.port)
        self.client.subscribe(mqtt_topic)
        self.client.loop_forever()

    def get_connection_message(self, rc) -> str:
        if rc == 0:
            return "MQTT CLIENT - Connection successful"
        if rc == 1:
            return "MQTT CLIENT - Connection refused - incorrect protocol version"
        if rc == 2:
            return "MQTT CLIENT - Connection refused - invalid client identifier"
        if rc == 3:
            return "MQTT CLIENT - Connection refused - server unavailable"
        if rc == 4:
            return "MQTT CLIENT - Connection refused - bad username or password"
        if rc == 5:
            return "MQTT CLIENT - Connection refused - not authorised"

    def on_connect(self, client, userdata, flags, rc):
        logging.info("MQTT CLIENT - On Connect Status: "+ self.get_connection_message(rc))    

    def on_disconnect(self, client, userdata, rc):
        logging.info("MQTT CLIENT - On Disconnect Status: "+ self.get_connection_message(rc))        
        self.client.connect(self.host, port=self.port) 
