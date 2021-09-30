from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/hello/")
def hello():
    return "Hello World"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye World"

@app.route("/private")
def private():
    return redirect(url_for('login'))

@app.route("/login")
def login():
    return "Username and Password"

@app.route("/force404")
def force404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "Nope, 404.", 404

@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename='mask.jpg')
    end = '">'
    return start + url + end, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

