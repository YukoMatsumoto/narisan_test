from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    if request.method == "GET":
        return render_template("login2.html")


@app.route("/login_action", methods=["POST"])
def login():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)
