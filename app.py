from flask import Flask, make_response, render_template, Response
import utils

app = Flask(__name__)

@app.route("/")
def default():
    return make_response(render_template(r"index.html"))

@app.route("/test", methods=["GET"])
def test():
    return Response(str('python-test works!'), mimetype="text/plain")

@app.route("/joke")
def print_joke():
    return Response(utils.get_random_dad_joke())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
