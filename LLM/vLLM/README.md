
# vLLM

## Notes

1. 不同的 `vllm` Python version會影響Client傳送API的格式內容。
2. 如果圖片太大(像是png) 可以透過轉換成小圖片然後再轉base64傳送
3. Please use `Python3.10`
4. 如果GPU計算能力8以下，請用`-dtype=half`

## Usage

### Docker

I used this existing docker image as a based image. You can implement `launch.sh` to start a docker container.

```bash
docker run -itd --gpus=all \
	--restart always --name vllm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --shm-size=200GB \
    -p 8000:8000 \
    -it qwenllm/qwenvl:2-cu121 bash
```

Version:

- `vllm==0.6.0`

### Launch a server

```bash
vllm serve {model name}
```

- `--port`: to specify a port
- `{model name}`: Such as `Qwen/Qwen2-VL-7B-Instruct`

Ref: https://docs.vllm.ai/en/v0.4.3/models/engine_args.html

### Client Script

cURL:

```bash

# convert -resize 60% test1.png image1.jpg
start_time=$(date +%s)

image_file="image1.jpg"
base64_image=$(base64 -w 0 "$image_file")


curl http://0.0.0.0:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "Qwen/Qwen2-VL-7B-Instruct",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant and good at reading the text on image. Please extract the above item and their corresponding content from the input image and return them in json format."}, 
    {
      "role": "user", 
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/jpg;base64,'"${base64_image}"'"
          }
        },
        {
          "type": "text",
          "text": "You will receive an image which contains some items as follow: - ID card number - issue date in English - expiry date in English"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.8,
  "repetition_penalty": 1.05,
  "max_tokens": 512
}'
```

Python: check `main.py` file.