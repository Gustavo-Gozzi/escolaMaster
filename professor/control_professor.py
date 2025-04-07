from model_professor import lista_professores, professores_by_id, post_professor, put_professor, delete_professor
from flask import Blueprint, request, jsonify

professor_blueprint = Blueprint("professores", __name__)


@professor_blueprint.route('/professores', methods=['GET'])
def getProfessores():
    dados = lista_professores()
    return jsonify(dados)

@professor_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def getProfessoresByID(idProfessor):
    professor = professores_by_id(idProfessor)
    return jsonify(professor)

@professor_blueprint.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    professor = post_professor(dados)
    return jsonify(professor)

@professor_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def putProfessores(idProfessor):
    resposta = request.json
    professor = put_professor(idProfessor, resposta)
    return jsonify(professor)
    
            
@professor_blueprint.route('/professores/<int:idProfessor>', methods=["DELETE"])
def deleteProfessores(idProfessor):
    professor = delete_professor(idProfessor)
    return jsonify(professor)
