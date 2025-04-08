from flask import Flask, render_template, request
from core import Calculator

calc = Calculator()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        operation = request.form.get("operation")

        if operation == "add":
            result = calc.add(num1=num1, num2=num2)
        elif operation == "subtract":
            result = calc.sub(num1=num1, num2=num2)
        elif operation == "multiply":
            result = calc.multiply(num1=num1, num2=num2)
        elif operation == "divide":
            result = calc.division(num1=num1, num2=num2)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
