from flask import Flask, jsonify, request
from configuracao import app
from aluno.control_aluno import aluno_blueprint

app.register_blueprint(aluno_blueprint)

dicionario = {
    "Alunos": [
        {
            "id": 100,
            "nome": "Joao",
            "idade": 0,
            "data_nascimento": "2004-08-29",
            "nota_primeiro_semestre": 0,
            "nota_segundo_semestre": 0,
            "turma_id": 0
        }
    ],
    "Professores": [
        {
            "id": 100,
            "nome": "Caio",
            "idade": 0,
            "data_nascimento": "2000-03-16",
            "disciplina": "API",
            "salario": 5000
        }
    ],
    "Turma": [
        {
            "id": 100,
            "nome": "API",
            "turno": "Noturno",
            "professor_id": 1
        },
        {
            "id": 200,
            "nome": "MOBILE",
            "turno": "Noturno",
            "professor_id": 2
        }
    ]
}


# Seção Reseta

@app.route('/reseta', methods=['POST'])
def reseta():
    dados = dicionario
    dicionario["Alunos"].clear()
    dicionario["Turma"].clear()
    dicionario["Professores"].clear()
    return jsonify(dados)
    
@app.route('/reseta/alunos', methods=['POST'])
def resetaAlunos():
    dados = dicionario["Alunos"]
    dicionario["Alunos"].clear()
    return jsonify(dados)

@app.route('/reseta/turmas', methods=['POST'])
def resetaTurmas():
    dados = dicionario["Turma"]
    dicionario["Turma"].clear()
    return jsonify(dados)

@app.route('/reseta/professores', methods=['POST'])
def resetaPRofessores():
    dados = dicionario["Professores"]
    dicionario["Professores"].clear()
    return jsonify(dados)




@app.route('/turmas', methods=["GET"])
def getTurmas():
    turmas = dicionario["Turma"]
    return jsonify(turmas)

@app.route('/turmas/<int:idTurma>', methods=["GET"])
def getTurmasbyID(idTurma):
    turmas = dicionario["Turma"]
    for turma in turmas:
        if turma["id"] == idTurma:
            return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}),400

@app.route('/turmas', methods=["POST"])
def postTurmas():
    if empty("Professores"):
        return jsonify("Não é possível criar uma turma sem professores.")
    dados = request.json
    turmas = dicionario["Turma"]
    professores = dicionario["Professores"]

    try:
        professor_existe = False

        for professor in professores:
            if professor["id"] == dados["professor_id"]:
                professor_existe = True
                break  
        
        if not professor_existe:
            raise ValueError("Impossível criar turma sem um professor")

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    for turma in turmas:
        if turma["id"] == dados["id"]:
            return jsonify({"erro": "id já utilizada"}),400 

    turmas.append(dados)
    return jsonify(dados)

@app.route('/turmas/<int:idTurma>', methods=['PUT'])
def putTurma(idTurma):
    turmas = dicionario["Turma"]
    for turma in turmas:
        if turma["id"] == idTurma:
            resposta = request.json
            if turma["nome"] != resposta["nome"]:
                turma["nome"] = resposta["nome"]

            if turma["turno"] != resposta["turno"]:
                turma["turno"] = resposta["turno"]

            if turma["professor_id"] != resposta["professor_id"]:
                turma["professor_id"] = resposta["professor_id"]

            return jsonify(resposta)
    return jsonify({"erro": "Turma não encontrada"}),400

@app.route('/turmas/<int:idTurma>', methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = dicionario["Turma"]      
    for turma in turmas:                
        if turma["id"] == idTurma:      
            turmas.remove(turma)        
            resposta = "Turma deletada com sucesso!"
            return jsonify(resposta)
    else:
        return jsonify({"erro": "Turma não encontrada"}),400


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )