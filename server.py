# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/clipboard', methods=['GET', 'POST'])
def accessClipboard():
    contents = "Nothing to paste"
    if request.method == 'POST':
        with open('clipboard.txt', 'w') as f:
            f.write(request.form['value'] + '\n')
    if request.method == 'GET':
        with open('clipboard.txt', 'r') as f:
            contents = f.read()
            return contents
    return "Bad method."
