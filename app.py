from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def pagina1():
    return render_template("index.html")

@app.route("/pagina1")
def cursos():
    return render_template("pagina1.html")


@app.route("/pagina2")
def tabla2():
    return render_template("pagina2.html")


@app.route("/pagina3", methods=["GET", "POST"])
def comentar():

   
    if request.method == "GET":
        return render_template("pagina3.html")

    nombre = request.form["nombre"]
    mensaje = request.form["mensaje"]

    return render_template(
        "pagina4.html",
        nombre=nombre,
        mensaje=mensaje
    )


@app.route("/pagina4")
def parrafo():
    return render_template("pagina4.html")


if __name__ == "__main__":
    app.run(debug=True)