from flask import Flask, make_response, render_template, Response

import utils
from utils import *

app = Flask(__name__)

@app.route("/")
def default():
    return make_response(render_template(r"index.html"))

@app.route("/test1", methods=["GET"])
def test():
    return Response(str('python-test works!'), mimetype="text/plain")

@app.route("/random")
def get_number():
    return Response(str(utils.num_gen()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
