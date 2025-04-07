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
    return jsonify(turma)
            

@turma_blueprint.route('/turmas', methods=["POST"])
def postTurmas():
    turma = request.json
    dados = model_turma.post_turma(turma)
    return jsonify(dados)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def putTurma(idTurma):
    turma = request.json
    dados = model_turma.put_turma(idTurma, turma)
    return jsonify(dados)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = model_turma.deleteTurma(idTurma)
    return jsonify(turmas)
