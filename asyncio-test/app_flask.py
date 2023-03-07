import time
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def hello_world():
    current_thread = threading.current_thread().ident
    print('Current thread: ', current_thread)
    time.sleep(2)
    return str(current_thread)

app.run(port=5001)