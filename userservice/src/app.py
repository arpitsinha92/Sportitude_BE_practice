from flask import Flask, request, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/api/<username>', methods=['GET'])
def hello(username):
    return jsonify({ "name":escape(username), "age":28, "city":"New York"})


app.run()