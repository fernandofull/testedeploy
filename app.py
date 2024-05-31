from flask import Flask
# converte dicionário em json
from flask import jsonify 
#  auxilia no recebimentos de dados na rota post
from flask import request
from flask import render_template, request, redirect


app = Flask(__name__)

produtos = {
    "nome": ["pão", "manteiga", "leite"],
    "preco": [3, 13, 8]
}

@app.route("/", methods=["GET"])
def lista_produtos():
    return jsonify(produtos)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)