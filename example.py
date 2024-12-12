# test_app.py
from mqtt_base_client import MQTTBaseClient

client = MQTTBaseClient(client_id="TestClient", broker="localhost", port=1883)
client.connect()
client.subscribe("test/topic")
client.publish("test/topic", {"key": "value"})
