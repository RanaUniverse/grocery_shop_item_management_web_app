"""
This is main.py file here i will write the flask logic to
run the main idea of the web application
"""

import sys

sys.dont_write_bytecode = True
# This upper two line help to stop making the .pyc file to looks clean the repo


from flask import Flask

app = Flask(__name__)


@app.get("/")
def index_page():
    return "<h1>Rana Universe</h1>"


if __name__ == "__main__":

    # This is running a demo development server
    app.run(
        host="0.0.0.0",
        port=9999,
        debug=True,
    )
