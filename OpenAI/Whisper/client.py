import requests

def send_wav_to_server(filename):
    url = "http://0.0.0.0:5566/upload" 
    
    with open(filename, 'rb') as wav_file:
        files = {'file': (filename, wav_file, 'audio/wav')}
        response = requests.post(url, files=files)

    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to upload WAV file to the server."

if __name__ == "__main__":
    wav_filename = "data/en-US_sample.wav" 
    server_response = send_wav_to_server(wav_filename)
    print("Server Response:", server_response)
