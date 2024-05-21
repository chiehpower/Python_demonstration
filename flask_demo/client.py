import requests
import time

start = time.time()

files = {'files': open('test.png', 'rb')}

ip = ''  # your server ip
url = 'http://{}:5001/normal_sending'.format(ip)

result = requests.post(url, files=files)
print(result.json())
print("Total time: ", time.time() - start)
