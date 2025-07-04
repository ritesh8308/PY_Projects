from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    expression = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        try:
            calc = Calculator(expression)
            result = calc.result
        except Exception as e:
            error = str(e)
    return render_template("index.html", result=result, error=error, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
