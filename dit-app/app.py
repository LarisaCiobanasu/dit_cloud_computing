import socket
import multiprocessing
import json
from flask import Flask, jsonify, render_template
app = Flask(__name__)



@app.route('/')
def index():

    data = {}
    data['hostname'] = socket.gethostname()
    data['ip_address'] = socket.gethostbyname(socket.gethostname())
    data['cpuCount'] = multiprocessing.cpu_count()  
    
    jsonData = json.dumps(data)

    def testFunc(t):
        return t+2



    return render_template('home.html',**locals())




if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)