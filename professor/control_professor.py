from professor import model_professor
from flask import Blueprint, request, jsonify

professor_blueprint = Blueprint("professores", __name__)


@professor_blueprint.route('/professores', methods=['GET'])
def getProfessores():
    dados = model_professor.lista_professores()
    return jsonify(dados)

@professor_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def getProfessoresByID(idProfessor):
    professor = model_professor.professores_by_id(idProfessor)
    try:
        return jsonify(professor["msg"]), professor["erro"]
    except:
        return jsonify(professor)

@professor_blueprint.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    professor = model_professor.post_professor(dados)
    try:
        return jsonify(professor["msg"]), professor["erro"]
    except:
        return jsonify(professor)

@professor_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def putProfessores(idProfessor):
    resposta = request.json
    professor = model_professor.put_professor(idProfessor, resposta)
    try:
        return jsonify(professor["msg"]), professor["erro"]
    except:
        return jsonify(professor)
    
            
@professor_blueprint.route('/professores/<int:idProfessor>', methods=["DELETE"])
def deleteProfessores(idProfessor):
    professor = model_professor.delete_professor(idProfessor)
    try:
        return jsonify(professor["msg"]), professor["erro"]
    except:
        return jsonify(professor)

@professor_blueprint.route('/reseta/professores', methods=['POST'])
def resetaPRofessores():
    dados = model_professor.reseta_Professores()
    return jsonify(dados)