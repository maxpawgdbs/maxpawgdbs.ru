import flask
import dotenv
import os

app = flask.Flask(__name__, template_folder=os.getcwd() + "/templates", static_folder=os.getcwd() + "/static")

dotenv.load_dotenv(".env")
PORT = os.getenv("PORT", None)
if PORT is None:
    print("нет порта")
    exit(0)


@app.get("/")
def main():
    return flask.render_template("main.html")


if __name__ == "__main__":
    app.run("0.0.0.0", PORT)
