from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alunos', methods=['GET'])
def getAlunos():
    dados = {
        "id": 1,
        "nome": "Mikael"
    }
    return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True)