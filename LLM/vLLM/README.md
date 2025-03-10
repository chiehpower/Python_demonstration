
# vLLM

## Notes

1. Different versions of `vllm` for Python might affect the API format sent by the client.  
2. If an image is too large (e.g., a PNG file), you can resize it to a smaller image and then convert it to Base64 for transmission.  
3. Please use **Python 3.10**.  
4. If your GPU compute capability is below 8, use the argument `--dtype=half`.  
5. Adjust the argument `--max_model_len` that can save some memory. However, it will impact the total number of tokens (Input + Output).
6. Adjust the arguemnt `--cpu-offload-gb` that it can move some computations in the CPU. (The inference speed will be slower.)

## Usage

### Docker

I used an existing Docker image as the base image. You can implement a `launch.sh` script to start the Docker container.  

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

### Launch a Server

```bash
vllm serve {model_name}
```

- `--port`: Specify a custom port.
- `{model name}`: For example, `Qwen/Qwen2-VL-7B-Instruct`

For more details, refer to the documentation: [vLLM Engine Arguments](https://docs.vllm.ai/en/v0.4.3/models/engine_args.html).

### Client Script

Using cURL:

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

Using Python
Refer to the `main.py` file for an example.

---

## Additional Version Information

Version:

- `vllm==0.6.4.post1`

1. Install vllm by python pip install

    ```
    sudo pip3 install vllm
    ```

2. Launch the server and try using the `Qwen/Qwen2-VL-2B-Instruct` model. It requires approximately 8GB of GPU memory:

    ```
    vllm serve Qwen/Qwen2-VL-2B-Instruct --dtype=half 
        --allowed-local-media-path=/to/folder/path
    ```

    >To change the port, use the `--port {number}` argument.

   - Additional info: https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html

3. [Client] Test it by curl

```bash
curl http://0.0.0.0:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "Qwen/Qwen2-VL-2B-Instruct",
  "messages": [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."}, 
    {
      "role": "user", 
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "file:///to/folder/path/image.png"
          }
        },
        {
          "type": "text",
          "text": "please extract information in this image?"
        }
      ]
    }
  ]
}'
```

---


## microsoft/Phi-3.5-vision-instruct

Server:

```bash
vllm serve --port 7861 microsoft/Phi-3.5-vision-instruct \
				   --trust-remote-code  
				   --disable_sliding_window 
				   --gpu-memory-utilization=0.9 
				   --max-model-len=73600
```

- gpu memory: 38537MiB / 40960MiB
- vllm version: 0.6.0
- model name: `microsoft/Phi-3.5-vision-instruct`

Clinet script:

---

## Qwen/Qwen2.5-VL-7B-Instruct

### Pre-requisite:

- Python Version: ≥ 3.9

### Docker

```bash
docker pull qwenllm/qwenvl:2.5-cu121


docker run -itd --gpus=all \
	--restart always --name vllm_qwen_test_2 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --shm-size=200GB \
  -p 8000:8000 \
  -it qwenllm/qwenvl:2.5-cu121 vllm serve --port 8000 Qwen/Qwen2.5-VL-7B-Instruct --max_model_len=32768
```

### Client

```bash
start_time=$(date +%s)

image_file="image2.jpg"
base64_image=$(base64 -w 0 "$image_file")


curl http://0.0.0.0:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "Qwen/Qwen2.5-VL-7B-Instruct",
  "messages": [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."}, 
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
          "text": "please extract information in this image?"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.8,
  "repetition_penalty": 1.05,
  "max_tokens": 512
}'

end_time=$(date +%s)
elapsed_time=$((end_time - start_time))
echo "Elapsed time: $elapsed_time seconds"
```
