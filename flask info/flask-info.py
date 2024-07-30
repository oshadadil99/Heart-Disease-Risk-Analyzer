from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/page1')
def page1():
    return "This is page   1"

@app.route('/page2')
def page2():
    return render_template('test-template.html')

app.run(debug=True)