import paho.mqtt.client as mqtt
import time
import random

# Define MQTT parameters
mqtt_broker = "mqtt.eclipse.org"  # Replace with your MQTT broker address
mqtt_port = 1883  # MQTT default port

# Generate some example environmental data
def generate_environmental_data():
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 70), 2)
    return {"temperature": temperature, "humidity": humidity}

# Create an MQTT client
client = mqtt.Client("IoTDevice1")  # Replace with a unique device ID

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Connection failed with code {rc}")

# Connect to the MQTT broker
client.on_connect = on_connect
client.connect(mqtt_broker, mqtt_port, keepalive=60)

# Main loop to send data periodically
try:
    while True:
        data = generate_environmental_data()
        client.publish("environmental_data", payload=str(data))
        print(f"Published: {data}")
        time.sleep(5)  # Adjust the interval as needed
except KeyboardInterrupt:
    print("Script terminated")

# Disconnect from the MQTT broker on script exit
client.disconnect()