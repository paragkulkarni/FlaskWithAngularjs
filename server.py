from flask import Flask, render_template
from flask_triangle import Triangle


app = Flask(__name__, static_path='/static')
Triangle(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
