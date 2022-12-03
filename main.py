from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return "hello world"

@app.route('/image_sample')
def image():
    return f"<img src={url_for('static', filename='images/students.jpg')} alt='Картинка'>"

if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')