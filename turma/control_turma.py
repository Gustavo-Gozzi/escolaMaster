from turma import model_turma
from flask import Blueprint, request, jsonify

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route('/turmas', methods=["GET"])
def getTurmas():
    turmas = model_turma.lista_turmas()
    return jsonify(turmas)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=["GET"])
def getTurmasbyID(idTurma):
    turma = model_turma.turma_by_id(idTurma)
    numero = 200
    if turma == "Turma não encontrada":
        numero = 400
    return jsonify(turma), numero
            

@turma_blueprint.route('/turmas', methods=["POST"])
def postTurmas():
    turma = request.json
    dados = model_turma.post_turma(turma)
    numero = 400
    if dados == "Turma adicionada com sucesso":
        numero = 200
    return jsonify(dados), numero

@turma_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def putTurma(idTurma):
    turma = request.json
    dados = model_turma.put_turma(idTurma, turma)
    numero = 400
    if dados == "Alteração realizada com sucesso!":
        numero = 200
    return jsonify(dados), numero

@turma_blueprint.route('/turmas/<int:idTurma>', methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = model_turma.deleteTurma(idTurma)
    numero = 400
    if turmas == "Turma deletada com sucesso!":
        numero = 200
    return jsonify(turmas), numero

@turma_blueprint.route('/reseta/turmas', methods=['POST'])
def resetaTurmas():
    dados = model_turma.reseta_Turmas()
    return jsonify(dados)