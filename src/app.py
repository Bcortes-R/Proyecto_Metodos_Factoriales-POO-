from flask import Flask, render_template, request
from controller import metFactoriales_controller

app = Flask(__name__, template_folder="view")


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        operacion = request.form["operacion"]
        try:
            x = float(request.form["valor_x"])
            resultado = metFactoriales_controller.calcular(operacion, x)
        except ValueError:
            resultado = "Error: El valor ingresado no es un número"
    return render_template("metFactoriales_view.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)

