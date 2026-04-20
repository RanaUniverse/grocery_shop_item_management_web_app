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
