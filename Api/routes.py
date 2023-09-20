from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    pass


if __name__ == '__main__':
    app.run(debug=True)
