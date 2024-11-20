# Qwen2

Model name: Qwen/Qwen2-7B-Instruct-GPTQ-Int8

Ref: https://huggingface.co/Qwen/Qwen2-7B-Instruct-GPTQ-Int8

### Steps:

1. `git clone git@hf.co:Qwen/Qwen2-7B-Instruct-GPTQ-Int8`

---

## vLLM

https://qwen.readthedocs.io/en/latest/deployment/vllm.html

### Steps:

```
sudo python3.10 -m pip install nvidia-ml-py
sudo python3.10 -m pip install vllm
```

### Usage

```
sudo python3.10 -m vllm serve Qwen/Qwen2.5-7B-Instruct 
```

### Troubleshooting

```
The error you're encountering is related to the use of Bfloat16 precision, which is only supported on GPUs with a compute capability of at least 8.0. However, your NVIDIA TITAN V GPU has a compute capability of 7.0, meaning it does not support Bfloat16. You can resolve this by using float16 precision instead, which is supported by your GPU.
```

---
## Github Version

Repo: https://github.com/QwenLM/Qwen2-VL


### Docker

Ref: https://github.com/QwenLM/Qwen2-VL#-docker

```
docker run --gpus all --ipc=host --network=host --rm --name qwen2 -it qwenllm/qwenvl:2-cu121 bash
```

Launch server:

```
python3 web_demo_mm.py
```
