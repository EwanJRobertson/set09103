from flask import Flask, render_template
app = Flask(__name__)

@app.route('/inherits/')
def inherits():
    return render_template('inheritance-main.html')

@app.route('/inherits/one')
def inherits_one():
    return render_template('inheritance-one.html')

@app.route('/inherits/two')
def inherits_two():
    return render_template('inheritance-two.html')
