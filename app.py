from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'my name is arshad and this is my argo cd project'
