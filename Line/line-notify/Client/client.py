import requests

if __name__ == '__main__':

    url = 'http://0.0.0.0:5555/sending_notify'

    result = requests.get(url)
    results = result.content