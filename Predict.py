import random
import json

# Load label mapping
with open('label_map.json') as f:
    label_map = json.load(f)

def predict_traffic(image_path):
    # In real use: Load model and process image
    prediction = random.choice(list(label_map.values()))
    return prediction
