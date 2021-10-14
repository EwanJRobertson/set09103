from flask import Flask, render_template
app = Flask(__name__)

@app.route('/collection/')
def collection():
    names = ['simo','thomo','lee','james']
    return render_template('collection.html', names=names)

if __name__ == 'main':
    app.run(host='0.0.0.0', debug=True)
