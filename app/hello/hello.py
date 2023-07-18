from flask import Flask, request, jsonify
from markupsafe import escape

app = Flask(__name__)
name="world"

@app.route('/', methods=['GET'])
@app.route('/<name>', methods=['GET'])
def hello(name=name):
    return f'Hello, {escape(name.capitalize())}!'

if __name__=="__main__":
    app.run(debug=True)
