from flask import Flask, jsonify, request
from configuracao import app
from aluno.control_aluno import aluno_blueprint
from professor.control_professor import professor_blueprint
from turma.control_turma import turma_blueprint
from reseta.control_reseta import reseta_blueprint

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )