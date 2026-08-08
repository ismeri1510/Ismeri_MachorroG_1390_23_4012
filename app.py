from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def pagina1():
    return render_template("index.html")

@app.route("/pagina1")
def prueba():
    return render_template("pagina1.html")


@app.route("/pagina2")
def tabla2():
    return render_template("pagina2.html")


@app.route("/pagina3", methods=["GET", "POST"])
def pagina3():

    # GET: muestra el formulario
    if request.method == "GET":
        return render_template("pagina3.html")

    # POST: recibe los datos del formulario
    nombre = request.form["nombre"]
    mensaje = request.form["mensaje"]

    # Envía los datos a pagina4.html
    return render_template(
        "pagina4.html",
        nombre=nombre,
        mensaje=mensaje
    )


@app.route("/pagina4")
def pagina4():
    return render_template("pagina4.html")


if __name__ == "__main__":
    app.run(debug=True)