from flask import Blueprint, request, jsonify
from reseta import model_reseta

reseta_blueprint = Blueprint("reseta", __name__)

@reseta_blueprint.route('/reseta', methods=['POST'])
def reseta():
    dados = model_reseta.reseta_all()
    return jsonify(dados)
