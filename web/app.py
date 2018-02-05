import os
from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

# Get parent directory's path
this_dir = os.path.dirname(os.path.abspath(__file__))


class FileNotFound(Exception):
    pass

@app.errorhandler(FileNotFound)
def file_not_found_error_handler(error):

    return make_response(render_template("404.html"),
        404 
    )


class FileForbidden(Exception):
    pass

@app.errorhandler(FileForbidden)
def file_forbidden_error_handler(error):
    return make_response(
        render_template("403.html"),
        403
    )


@app.route("/")
def hello():
    return "UOCIS docker demo!"


@app.route(methods=['GET', 'Post'])
def fetch_html(file_name):

    file_path = os.path.join(this_dir, "templates", file_name)

    if os.path.isfile(file_path) is True:

        return make_response(
            render_template(file_name),
            200  # OK
        )
    else:
        raise FileNotFound



# Start the server
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
