from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Word!!"

@app.route("/produto/<id>")
def ConsultarProduto(id):
    Produto = ""
    if id == "10":
        Produto = "Camisa"

    if id == "20":
        Produto = "Bermuda"

    return render_template("index.html",produtoEncontrado = Produto)

if __name__ == "__main__":
    app.run(debug=True)



    