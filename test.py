from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def index():
    return render_template("login2.html")


@app.route("/login_action", methods=["POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        if password == "password":
            return render_template("test.html")
        else:
            return render_template("login2.html")


if __name__ == "__main__":
    app.run(debug=True)