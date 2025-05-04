from flask import Blueprint, request, jsonify
from aluno import model_aluno
aluno_blueprint = Blueprint("alunos", __name__)

@aluno_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(model_aluno.lista_alunos())

@aluno_blueprint.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunosbyID(idAluno):
    aluno = model_aluno.aluno_by_id(idAluno)
    try:
        return jsonify(aluno["msg"]), aluno["erro"]
    except: 
        return jsonify(aluno)

@aluno_blueprint.route('/alunos', methods=["POST"])
def postAlunos():
    dados = request.json
    aluno = model_aluno.post_alunos(dados)
    try:
        return jsonify(aluno["msg"]), aluno["erro"]
    except: 
        return jsonify(aluno)

@aluno_blueprint.route('/alunos/<int:idAluno>', methods=["PUT"])
def putAlunos(idAluno):
    resposta = request.json
    aluno = model_aluno.put_Alunos(idAluno, resposta)
    try:
        return jsonify(aluno["msg"]), aluno["erro"]
    except: 
        return jsonify(aluno)

@aluno_blueprint.route('/alunos/<int:idAluno>', methods=["DELETE"])
def deleteAlunos(idAluno):
    aluno = model_aluno.delete_aluno(idAluno)
    try:
        return jsonify(aluno["msg"]), aluno["erro"]
    except: 
        return jsonify(aluno)

@aluno_blueprint.route('/reseta/alunos', methods=['POST'])
def reseta_Alunos():
    dados = model_aluno.resetaAlunos()
    return jsonify(dados)