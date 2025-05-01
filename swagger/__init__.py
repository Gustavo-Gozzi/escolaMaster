from flask_restx import Api

# Inicializa o objeto API do Swagger
api = Api(
    version="1.0",
    title="API da Escola Master",
    description="Documentação da API Escola Master para Alunos, Professores e Turmas",
    doc="/docs",
    mask_swagger=False,  # Desativa o X-Fields no Swagger,
    prefix="/api"
)