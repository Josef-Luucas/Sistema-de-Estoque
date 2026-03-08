from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        'id': 1,
        'produto': 'Bolacha Mini Maria Zero lactose Mauricéa 180g',
        'quantidade(uni)': 20,
        'valor': 'R$:3,45'
    },
    {
        'id': 2,
        'produto': 'Bolacha Cream Cracker Vitarella Trad. 160g',
        'quantidade(uni)': 32,
        'valor': 'R$:3,10'
    },
    {
        'id': 3,
        'produto': 'Biscoito Treloso Recheado Chocolate 37g',
        'quantidade(uni)': 58,
        'valor': 'R$:0,65'
    },
]

#consultar todos
@app.route('/estoque',methods=['GET'])
def ver_prod():
    return jsonify(produtos)

#consultar individual
@app.route('/estoque/<int:id>',methods=['GET'])
def ver_prod_indiv(id):
    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)
        
#editar produto
@app.route('/estoque/<int:id>',methods=['PUT'])
def editar_prod(id):
    prod_alterado = request.get_json()
    for indice,produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(prod_alterado)
            return jsonify(produtos[indice])
        
#criar produto
@app.route('/estoque',methods=['POST'])
def novo_prod():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify(produtos)

#excluir produto
@app.route('/estoque/<int:id>',methods=['DELETE'])
def excluir_prod(id):
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]
    return jsonify(produtos)        
        

app.run(port=5000,host='localhost', debug=True )