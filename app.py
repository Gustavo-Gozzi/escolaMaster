from flask import Flask, jsonify, request

app = Flask(__name__)

dicionario = {
    "Alunos": [
        {
            "id": 1,
            "nome": "Daniel"
        }
    ],
    "Professores": [
        {
            "id": 1,
            "nome": "Caio"
        }
    ]
}

# Seção Alunos

@app.route('/alunos', methods=['GET'])
def getAlunos():
    dados = dicionario["Alunos"]
    return jsonify(dados)

@app.route('/alunos', methods=["POST"])
def postAluno():
    dados = request.json
    alunos = dicionario["Alunos"]
    alunos.append(dados)
    return jsonify(dados)

# Seção Professores

@app.route('/professores', methods=['GET'])
def getProfessores():
    dados = dicionario["Professores"]
    return jsonify(dados)

@app.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    alunos = dicionario["Professores"]
    alunos.append(dados)
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)