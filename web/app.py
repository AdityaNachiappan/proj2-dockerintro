import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!"


@app.route("/name")
def hello():
    if os.path.isfile("./templates/" + name):
		return render_template(name), 200
    elif "//" in name or ".." in name or "~" in name :
        abort(403)
    elif  ".html" not in name and ".css" not in name:
        abort(404)
  

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'),404

@app.errorhandler(403)
def page_not_found(error):
	return flask.render_template('403.html'),403	


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
