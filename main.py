import flask
import datetime
import dotenv
import os

app = flask.Flask(__name__)

dotenv.load_dotenv(".env")
PORT = os.getenv("PORT", None)
if PORT is None:
    print("нет порта")
    exit(0)


@app.get("/")
def main():
    return "Hello World!\n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 200


if __name__ == "__main__":
    app.run("0.0.0.0", PORT)
