#!/bin/bash

docker run -itd --name=ollama --gpus '"device=GPU-d95965943d"' --shm-size=150GB \
    -v ollama:/root/.ollama -p 8001:11434 \
    ollama/ollama:0.4.0-rc6
