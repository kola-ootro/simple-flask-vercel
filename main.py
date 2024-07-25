from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Vercel!"

@app.route('/test')
def test():
    return "Test route is working"