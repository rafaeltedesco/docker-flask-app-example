import os
from flask import Flask

PORT = os.environ.get('PORT', 3000)
APP_NAME = os.environ.get('APP_NAME', 'Default flask')

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return f'<h1>Hello World From {APP_NAME} On PORT {PORT}</h1>'
