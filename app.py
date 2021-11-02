from flask import Flask, jsonify, make_response, render_template

app = Flask(__name__)


@app.route("/")
def default():
    return make_response(render_template(r"index.html"))


@app.route("/test", methods=["GET"])
def test():
    return jsonify(success=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
