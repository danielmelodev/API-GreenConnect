from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message='Hello, world!')

@app.route('/ecoloja')
def eco():
    loja = {'id': 1, 'nome': 'ecoloja', 'endereco': 'rua do hospicio, n33a', 'segmento': 'organicos'}
    return jsonify(loja)

@app.route('/teste')
def teste():
    content1 = {'title': 'Conteudo 1', 'description': 'Este e o conteudo 1'}
    content2 = {'title': 'Conteudo 2', 'description': 'Este e o conteudo 2'}
    content3 = {'title': 'Conteudo 3', 'description': 'Este e o conteudo 3'}

    resultado = [content1, content2, content3]


    return jsonify(resultado)


if __name__ == '__main__':
    app.run()
