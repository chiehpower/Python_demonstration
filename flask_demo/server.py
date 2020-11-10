import time
from flask import Flask, request, jsonify
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
        if 'file' not in request.files:
           return "someting went wrong 1"
           
    print('request files checking takes: ', time.time()-start_pre, flush=True)
    return jsonify({
        'result':'Get to the devel'
    })

if __name__ == '__main__':
    # This is used when running locally.
    app.run(host='0.0.0.0',port=5001, debug=True)