curl http://0.0.0.0:8001/api/generate -d '{                                                                                       
  "model": "llama3.1",
  "prompt": "Why is the sky blue?",
  "stream": false,
  "options": {
    "top_k": 20,
    "temperature": 0.8
  }
}'