from flask import Flask, redirect, url_for, abort, request
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    name = request.args.get("name","")
    if name == None:
        return "no param supplied"
    elif name == "":
        return "Hello world"
    else:
        return "Hello %s" % name

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

@app.route("/account/", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        f = request.files['datafile']
        f.save("static/uploads/upload.png")
        return "File Uploaded"
    else:
        page = '''
        <html>
            <body>
                <form action='' method='post' name='form' enctype='multipart/form-data'>
                    <input type='file' name='datafile' />
                    <input type='submit' name='submit' id='submit' />
                </form>
            </body>
        </html>
        '''

        return page

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

