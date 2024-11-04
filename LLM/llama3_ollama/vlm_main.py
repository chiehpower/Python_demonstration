import requests
import base64
import json
import time

image_file = "test1.png"

with open(image_file, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode('utf-8')

payload = {
    "model": "x/llama3.2-vision:11b-instruct-q4_K_M",
    "prompt": "Please extract the information and tell me the information.",
    "stream": False,
    "images": [base64_image]
}

url = "http://0.0.0.0:8001/api/generate"

start_time = time.time()
response = requests.post(url, json=payload)
if response.status_code == 200:
    print(json.dumps(response.json()['response'], indent=2))
    end_time = time.time() - start_time
    print(f"Total time takes :{end_time}")
else:
    print(f"Failed: {response.status_code}")
    print(response.text)

