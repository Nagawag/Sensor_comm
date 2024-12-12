import json
import paho.mqtt.client as mqtt
import time

class MQTTBaseClient:
    def __init__(self, client_id, broker='localhost', port=1883):
        # Include the callback_api_version when creating the client
        self.client = mqtt.Client(client_id, callback_api_version="v2.0")
        self.broker = broker
        self.port = port

        # Assign callback functions here
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):
        """Connects to the MQTT broker and starts the network loop."""
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()  # Starts the loop in the background
            print(f"{self.client._client_id.decode()} connected to broker")
        except Exception as e:
            print(f"Error connecting to broker: {e}")

    def on_connect(self, client, userdata, flags, rc):
        """Handles connection events to the broker."""
        if rc == 0:
            print(f"{client._client_id.decode()} connected successfully")
        else:
            print(f"Connection failed with result code {rc}")

    def on_message(self, client, userdata, msg):
        """Handles incoming messages (default implementation)."""
        print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

    def subscribe(self, topic):
        """Subscribes to a specific topic."""
        self.client.subscribe(topic)

    def publish(self, topic, payload):
        """Publishes a message to a specific topic, encoding it as JSON."""
        self.client.publish(topic, json.dumps(payload))
