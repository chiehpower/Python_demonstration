# Whisper

Repo: https://github.com/openai/whisper

## Testing env 

- Ubuntu 20.04

## Installation 

```
pip install -U openai-whisper

pip install setuptools-rust
sudo apt update && sudo apt install ffmpeg
```


## Model size

Refer from the official repo.

| Size   | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
| ------ | ---------- | ------------------ | ------------------ | ------------- | -------------- |
| tiny   | 39 M       | `tiny.en`          | `tiny`             | ~1 GB         | ~32x           |
| base   | 74 M       | `base.en`          | `base`             | ~1 GB         | ~16x           |
| small  | 244 M      | `small.en`         | `small`            | ~2 GB         | ~6x            |
| medium | 769 M      | `medium.en`        | `medium`           | ~5 GB         | ~2x            |
| large  | 1550 M     | N/A                | `large`            | ~10 GB        | 1x             |

You can try with different model. Very simple.

## Usage


I attach the audio files in the `data` folder.
```
python main.py
```

# Deploy on the server endpoint

## Server side

```
cd Server

python3 app.py
```

## Client side

```
python3 client.py
```