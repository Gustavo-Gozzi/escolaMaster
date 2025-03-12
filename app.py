from flask import Flask, jsonify

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
            "id": "pr01",
            "nome": "Caio"
        }
    ]
}

@app.route('/alunos', methods=['GET'])
def getAlunos():
    dados = dicionario["Alunos"]
    return jsonify(dados)

@app.route('/alunos', methods=["POST"])
def postAluno():
    novo_aluno = {
        "id": 2,
        "nome": "Frodo"
    }
    
    dados = dicionario["Alunos"]
    dados.append(novo_aluno)
    return jsonify(dados)
    

if __name__ == '__main__':
    app.run(debug=True)