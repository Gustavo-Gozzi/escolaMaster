from turma import modelo_turma
from flask import Blueprint, request, jsonify

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route('/turmas', methods=["GET"])
def getTurmas():
    turmas = modelo_turma.lista_turmas()
    return jsonify(turmas)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=["GET"])
def getTurmasbyID(idTurma):
    turma = modelo_turma.turma_by_id(idTurma)
    return jsonify(turma)
            

@turma_blueprint.route('/turmas', methods=["POST"])
def postTurmas():
    turma = request.json
    dados = modelo_turma.post_turma(turma)
    return jsonify(dados)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def putTurma(idTurma):
    turma = request.json
    dados = modelo_turma.put_turma(idTurma, turma)
    return jsonify(dados)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = modelo_turma.deleteTurma(idTurma)
    return jsonify(turmas)
