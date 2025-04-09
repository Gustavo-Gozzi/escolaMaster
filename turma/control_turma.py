from turma import model_turma
from flask import Blueprint, request, jsonify

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route('/turmas', methods=["GET"])
def getTurmas():
    turma = model_turma.lista_turmas()
    return jsonify(turma)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=["GET"])
def getTurmasbyID(idTurma):
    turma = model_turma.turma_by_id(idTurma)
    try:
        return jsonify(turma["msg"]), turma["erro"]
    except:
        return jsonify(turma)
            

@turma_blueprint.route('/turmas', methods=["POST"])
def postTurmas():
    dados = request.json
    turma = model_turma.post_turma(dados)
    try:
        return jsonify(turma["msg"]), turma["erro"]
    except:
        return jsonify(turma)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def putTurma(idTurma):
    dados = request.json
    turma = model_turma.put_turma(idTurma, dados)
    try:
        return jsonify(turma["msg"]), turma["erro"]
    except:
        return jsonify(turma)

@turma_blueprint.route('/turmas/<int:idTurma>', methods=["DELETE"])
def deleteTurma(idTurma):
    turma = model_turma.deleteTurma(idTurma)
    try:
        return jsonify(turma["msg"]), turma["erro"]
    except:
        return jsonify(turma)

@turma_blueprint.route('/reseta/turmas', methods=['POST'])
def resetaTurmas():
    dados = model_turma.reseta_Turmas()
    return jsonify(dados)