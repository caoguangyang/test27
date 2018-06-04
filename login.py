from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'

@app.route('/login')
def login():
    return "登录"

@app.route('/logout')
def logout():
    return "退出"

if __name__ == '__main__':
    app.run(debug=True)