from flask import Flask, jsonify, request
from configuracao import app, db
from aluno.control_aluno import aluno_blueprint
from professor.control_professor import professor_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from turma.control_turma import turma_blueprint
from reseta.control_reseta import reseta_blueprint

SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL,API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(aluno_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(turma_blueprint)
app.register_blueprint(reseta_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )