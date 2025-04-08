from flask import Blueprint, request, jsonify
from aluno import model_aluno
aluno_blueprint = Blueprint("alunos", __name__)


@aluno_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(model_aluno.lista_alunos())



@aluno_blueprint.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunosbyID(idAluno):
    aluno = model_aluno.aluno_by_id(idAluno)
    numero = 200
    if aluno == "Aluno não encontrado!":
        numero = 400
    return jsonify(aluno), numero



@aluno_blueprint.route('/alunos', methods=["POST"])
def postAlunos():
    dados = request.json
    aluno = model_aluno.post_alunos(dados)
    numero = 400
    if aluno == "Aluno adicionado com sucesso":
        numero = 200
    return jsonify(aluno), numero



@aluno_blueprint.route('/alunos/<int:idAluno>', methods=["PUT"])
def putAlunos(idAluno):
    resposta = request.json
    aluno = model_aluno.put_Alunos(idAluno, resposta)
    numero = 400
    if aluno == "Alteração realizada com sucesso!":
        numero = 200
    
    return jsonify(aluno), numero



@aluno_blueprint.route('/alunos/<int:idAluno>', methods=["DELETE"])
def deleteAlunos(idAluno):
    aluno = model_aluno.delete_aluno(idAluno)
    numero = 200
    if aluno == "Aluno não encontrado!":
        numero = 400
    return jsonify(aluno), numero

@aluno_blueprint.route('/reseta/alunos', methods=['POST'])
def reseta_Alunos():
    dados = model_aluno.resetaAlunos()
    return jsonify(dados)
