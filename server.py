from flask import Flask, render_template

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route("/")
def start_here():
    """bootstrap page."""

    return render_template("bootstrap.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')