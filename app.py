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
def postAlunos():
    dados = request.json
    alunos = dicionario["Alunos"]
    alunos.append(dados)
    return jsonify(dados)

@app.route('/alunos/<int:idAluno>', methods=["PUT"])
def putAlunos(idAluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:
            resposta = request.json
            aluno['nome'] = resposta['nome']
            return jsonify(resposta)
    return jsonify("Id do aluno não encontrado")

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