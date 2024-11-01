from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "Hello, World!"

@app.route('/')
def hello():
    return 'hello hayoung'