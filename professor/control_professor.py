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
    numero = 200
    if professor == "Professor não encontrado":
        numero = 400
    return jsonify(professor), numero

@professor_blueprint.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    professor = model_professor.post_professor(dados)
    numero = 400
    if professor == "Professor adicionado com sucesso!":
        numero = 200
    return jsonify(professor), numero

@professor_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def putProfessores(idProfessor):
    resposta = request.json
    professor = model_professor.put_professor(idProfessor, resposta)
    numero = 400
    if professor == "Alteração realizada com sucesso!":
        numero = 200
    return jsonify(professor), numero
    
            
@professor_blueprint.route('/professores/<int:idProfessor>', methods=["DELETE"])
def deleteProfessores(idProfessor):
    professor = model_professor.delete_professor(idProfessor)
    numero = 400
    if professor == "Professor deletado com sucesso!":
        numero = 200
    return jsonify(professor), numero

@professor_blueprint.route('/reseta/professores', methods=['POST'])
def resetaPRofessores():
    dados = model_professor.reseta_Professores()
    return jsonify(dados)