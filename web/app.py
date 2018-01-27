import os
from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

# Get parent directory's path
this_dir = os.path.dirname(os.path.abspath(__file__))


# Define a class to link with error handler
class FileNotFound(Exception):
    pass


# Declaring a error handler and linking with FileNotFound except class
@app.errorhandler(FileNotFound)
def file_not_found_error_handler(error):

    return make_response(  # Built in method to make response with required headers
        # Custom template stored in templates folder will be rendered in response
        render_template("404.html"),
        404  # 404 will be sent as error code among response headers
    )


# Same routine above but for a new type of exception
class FileForbidden(Exception):
    pass


@app.errorhandler(FileForbidden)
def file_forbidden_error_handler(error):
    return make_response(
        render_template("403.html"),
        403
    )


# Default page
@app.route("/")
def hello():
    return "UOCIS docker demo!"


# New method that gets called everytime we try to get a file
@app.route(  # Decorator that ties "/get/example.html" URL with fetch_html
    "/get/<file_name>",  
    methods=['GET', 'Post']  # Allowed method
)
# Gets invoked everytime "/get/example.html" endpoint gets pinged
def fetch_html(file_name):

    # Get file path from variable name with in endpoint url
    file_path = os.path.join(this_dir, "templates", file_name)

    # If file exists, render it and respond
    if os.path.isfile(file_path) is True:

        return make_response(
            render_template(file_name),
            200  # OK
        )
    # If it doesn't, raise FileNotFound exception.
    else:
        raise FileNotFound



# Start the server
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
