from flask import render_template, request, Flask
from calculator import CoupleCalculator

flask_app = Flask(__name__)


@flask_app.route("/couple-calculator", methods=["GET"])
def index():
    """Displaying the index page accessible at '/' """
    return render_template("index.html")


@flask_app.route("/couple-result", methods=["POST"])
def operation_result():
    """Route where we send calculator form input"""
    calculator = CoupleCalculator()
    name1 = request.form["name1"]
    name2 = request.form["name2"]
    result = calculator.calculate(name1, name2)
    return render_template("index.html", name1=name1, name2=name2, result=result, calculation_success=True)


if __name__ == "__main__":
    flask_app.debug = True
    flask_app.run()