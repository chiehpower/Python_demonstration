# Ollama with llama3

Docker usage

```
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Pull the llama3 model.

```
docker exec -ti ollama bash
ollama pull llama3
```

Test it.

```
curl http://0.0.0.0:11434/api/generate -d '{                            
  "model": "llama3",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

Or 

```
curl http://0.0.0.0:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ],
  "stream": false
}'
```

## Generate request (With options)

Reference: https://github.com/ollama/ollama/blob/main/docs/api.md#generate-request-with-options

It can allow to add some parameters.

```
curl http://0.0.0.0:11434/api/generate -d '{                                                                                       
  "model": "llama3",
  "prompt": "Why is the sky blue?",
  "stream": false,
  "options": {
    "num_keep": 5,
    "seed": 42,
    "num_predict": 100,
    "top_k": 20,
    "top_p": 0.9,
    "tfs_z": 0.5,
    "typical_p": 0.7,
    "repeat_last_n": 33,
    "temperature": 0.8,
    "repeat_penalty": 1.2,
    "presence_penalty": 1.5,
    "frequency_penalty": 1.0,
    "mirostat": 1,
    "mirostat_tau": 0.8,
    "mirostat_eta": 0.6,
    "penalize_newline": true,
    "stop": ["\n", "user:"],
    "numa": false,
    "num_ctx": 1024,
    "num_batch": 2,
    "num_gqa": 1,
    "num_gpu": 1,
    "main_gpu": 0,
    "low_vram": false,
    "f16_kv": true,
    "vocab_only": false,
    "use_mmap": true,
    "use_mlock": false,
    "rope_frequency_base": 1.1,
    "rope_frequency_scale": 0.8,
    "num_thread": 8
  }
}'
```