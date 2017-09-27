from flask import Flask
from controllers import users, records

app = Flask(__name__)


apps = [
    users.app,
    records.app,
]
for a in apps:
    app.register_blueprint(a)


@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
