from openai import OpenAI
import base64
import json

# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://0.0.0.0:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

image_path = "image1.png"

# 讀取圖像文件並進行 Base64 編碼
with open(image_path, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode('utf-8')


chat_response = client.chat.completions.create(
    model="Qwen/Qwen2-VL-7B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant and good at reading the text on image. Please extract the above item and their corresponding content from the input image and return them in json format."},
        {"role": "user",
                 "content": [
                     {
                         "type": "image_url",
                         "image_url": {"url": f"data:image/jpg;base64, ${base64_image}"}
                     },
                     {"type": "text",
                      "text": "You will receive an image which contains some items as follow: - ID card number - issue date in English - expiry date in English"}]
         }
    ],
    temperature=0.7,
    top_p=0.8,
    max_tokens=512,
    extra_body={
        "repetition_penalty": 1.05,
    },
)
response_message = chat_response.choices[0].message.content

response_message = response_message.strip('```json').strip()

response_message = json.loads(response_message)

print(json.dumps(response_message, indent=4, ensure_ascii=False))
