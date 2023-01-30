from flask import Flask, request, jsonify, Response, send_file
import requests
app = Flask(__name__)

@app.route('/sending_notify', methods=['GET'])
def sending_image():  
    if request.method == 'GET':

        key_ = ''
        headers = {
            "Authorization": "Bearer " + key_, 
            "Content-Type" : "application/x-www-form-urlencoded"
        }

        payload = {
            'message': 'Hi guys' 
        }

        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

        return Response('Done', mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555, debug=True)
