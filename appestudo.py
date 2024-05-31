from flask import Flask
# converte dicionário em json
from flask import jsonify 
#  auxilia no recebimentos de dados na rota post
from flask import request
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

produtos = {
    "nome": ["pão", "manteiga", "leite"],
    "preco": [3, 13, 8]
}

@app.route("/", methods=["GET"])
def lista_produtos():
    return jsonify(produtos)

# Criando rota personalizada para buscar individualmente cada produto 
# Dessa forma o que vier após a barra ficará no parametro da função. Ex. http://127.0.0.1:5000/0 vai trazer o índice 0 pela rota,
# vai entrar no parametro da função e vai parar no id da f'string para retornar o produto pão.

@app.route("/<int:id>")
def busca_produto(id):
    try:
        return f"Nome do produto: {produtos['nome'][id]} - Preço: R${produtos['preco'][id]}."
    except:
        return "Produto não encontrado!"

# Nas rotas post, o backend precisa estar esperando a rota. 
@app.route("/cadastrar_produto", methods=["POST"])
def cadastrar_produto():
    # dados vai conter os dados da rota, que nesse caso é um dicionário. 
    # request.get_json que receberá esses dados.
    dados = request.get_json()
    # appende de dados[nome] em produtos[nome]
    produtos["nome"].append(dados["nome"])
    produtos["preco"].append(dados["preco"])
    return f"Produto <{dados['nome']} cadastrado com sucesso!>"

@app.route("/atualizar_produto/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json()
    try:
        # o for está iterando na key e value do dicionário. sobre os itens (k + v) do dicionário que está armazenado na variavel dados.
        for k, v in dados.items():
            produtos[k][id] = dados[k]
        return 'Produto atualizado com sucesso!'
    except:
        return "Não foi possível atualizar o produto!"
    
@app.route("/apagar_produto/<int:id>", methods=["DELETE"])
def apagar_produto(id):
    try:
        del produtos["nome"][id]
        del produtos["preco"][id]
        return "Produto deletado com sucesso!"
    except:
        return "Não foi possível apagar o produto!"  
    
@app.route("/dados", methods=["GET", "POST" ])
def receber_dados():
    # o request.form é para receber todos os campos do formulário que vem na forma de um dicionário.
    dados = request.form
    print(dados['nome'])
    print(dados['cidade'])
    return render_template("receber_dados.html")

@app.route("/listar_produtos")
def listar_produtos():
    # produtos='PRODUTO' apenas criando a variável produto e atribuindo a esta a string PRODUTO que será utilizando no jinja no html.
    return render_template('listar_produtos.html', produtos=produtos["nome"])

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)