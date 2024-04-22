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