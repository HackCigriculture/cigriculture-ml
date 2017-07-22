import json
from flask import Flask, request
import numpy as np
from network import network

app = Flask(__name__)
model = network()
model.load_weights('model/1500722111.result')


@app.route('/', methods=['POST'])
def geo():
    body = request.get_json(silent=True, force=True)
    print(body)
    result = model.predict(np.array(body))
    return json.dumps(result.tolist())

if __name__ == '__main__':
    app.run()
