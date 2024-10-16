from main import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def madlib():
    if request.method == "POST":
        adj = request.form["adj"]
        verb1 = request.form["verb1"]
        verb2 = request.form["verb2"]
        verb3 = request.form["verb3"]

        madlib = f"""Heyy, I am so {adj}, and I was waiting for you like I
        have decided so many {verb1}, so be ready and watch {verb2}.
        Btw, I was worried about yesterday and {verb3}, thanks."""

        return render_template("index.html", madlib=madlib)

    # If the request method is GET, return the page without the madlib
    return render_template("index.html", madlib="")

if __name__ == "__main__":
    app.run(debug=True)
