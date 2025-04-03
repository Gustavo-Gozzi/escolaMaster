from flask import Blueprint, request, jsonify
from model.model_aluno import lista_alunos, aluno_by_id, post_alunos, put_Alunos, delete_aluno

aluno_blueprint = Blueprint("alunos", __name__)


@aluno_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(lista_alunos())



@aluno_blueprint.route('/alunos', methods=['GET'])
def getAlunosbyID(idAluno):
    aluno = aluno_by_id(idAluno)
    return jsonify(aluno)



@aluno_blueprint.route('/alunos', methods=["POST"])
def postAlunos():
    dados = request.json
    alunos = post_alunos(dados)
    return jsonify(alunos)



@aluno_blueprint.route('/alunos/<int:idAluno>', methods=["PUT"])
def putAlunos(idAluno):
    resposta = request.json
    aluno = put_Alunos(idAluno, resposta)
    return jsonify(aluno)



@aluno_blueprint.route('/alunos/<int:idAluno>', methods=["DELETE"])
def deleteAlunos(idAluno):
    aluno = delete_aluno(idAluno)
    return jsonify(aluno)