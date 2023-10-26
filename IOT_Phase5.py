import paho.mqtt.client as mqtt
import time
import random

# Define the MQTT broker information
broker_address = "mqtt.eclipse.org"
broker_port = 1883
topic = "environmental_data"

# Simulate data collection (replace with actual sensor readings)
def collect_environmental_data():
    temperature = random.uniform(15, 30)
    humidity = random.uniform(30, 60)
    air_quality = random.uniform(0, 100)
    noise_level = random.uniform(40, 80)
    return {
        "temperature": temperature,
        "humidity": humidity,
        "air_quality": air_quality,
        "noise_level": noise_level
    }

# Initialize the MQTT client
client = mqtt.Client("IoTDevice")
client.connect(broker_address, broker_port)

while True:
    data = collect_environmental_data()
    
    # Convert data to a JSON string
    data_json = json.dumps(data)
    
    # Publish data to the MQTT topic
    client.publish(topic, data_json)
    
    print("Data published:", data_json)
    
    time.sleep(60)  # Adjust the interval as needed

# You may need to handle exceptions and gracefully disconnect from the MQTT broker when needed.