from flask import Flask, jsonify, request
from configuracao import app
from aluno.control_aluno import aluno_blueprint
from professor.control_professor import professor_blueprint
from turma.control_turma import turma_blueprint

app.register_blueprint(aluno_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(turma_blueprint)


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


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )