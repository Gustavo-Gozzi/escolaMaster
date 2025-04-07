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
    return jsonify(professor)

@professor_blueprint.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    professor = model_professor.post_professor(dados)
    return jsonify(professor)

@professor_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def putProfessores(idProfessor):
    resposta = request.json
    professor = model_professor.put_professor(idProfessor, resposta)
    return jsonify(professor)
    
            
@professor_blueprint.route('/professores/<int:idProfessor>', methods=["DELETE"])
def deleteProfessores(idProfessor):
    professor = model_professor.delete_professor(idProfessor)
    return jsonify(professor)
