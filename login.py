from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'

@app.route('/')
def login():
    return "登录11"

if __name__ == '__main__':
    app.run(debug=True)