from flask import Flask, make_response, render_template, Response

app = Flask(__name__)

@app.route("/")
def default():
    return make_response(render_template(r"index.html"))

@app.route("/test", methods=["GET"])
def test():
    return Response(str('python-test works!'), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
