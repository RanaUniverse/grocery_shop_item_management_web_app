"""
This is main.py file here i will write the flask logic to
run the main idea of the web application
"""

import sys

sys.dont_write_bytecode = True
# This upper two line help to stop making the .pyc file to looks clean the repo


from flask import Flask


from blueprint.error.routes import error_bp
from blueprint.general.routes import general_bp


app = Flask(__name__)

app.register_blueprint(blueprint=general_bp)
app.register_blueprint(blueprint=error_bp)


if __name__ == "__main__":

    # This is running a demo development server
    app.run(
        host="0.0.0.0",
        port=9999,
        debug=True,
    )
