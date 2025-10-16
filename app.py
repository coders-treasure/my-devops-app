from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # This will be your simple application's response
    return '<h1>Hello DevOps Beginner! This is Version 1.0</h1>'

if __name__ == '__main__':
    # Flask runs on port 5000 by default
    app.run(debug=True, host='0.0.0.0', port=5000)