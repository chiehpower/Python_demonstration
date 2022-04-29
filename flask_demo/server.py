import time
from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/devel',  methods=['POST', 'GET'])
def devel():
    return jsonify({
        'result':'Get to the devel'
    })

@app.route('/normal_sending' ,methods=['POST'])
def predict():  
    start_pre = time.time()
    if request.method == 'POST':
        if 'files' not in request.files:
           return jsonify({
            'result':'someting went wrong 1'
        })

        npimg = np.fromstring(request.files["files"].read(), np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        print('request files checking takes: ', time.time()-start_pre, flush=True)
        return jsonify({
            'result':'Get to the devel'
        })

if __name__ == '__main__':
    # This is used when running locally.
    app.run(host='0.0.0.0',port=5001, debug=True)