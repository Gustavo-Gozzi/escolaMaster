# escolaMaster
Projeto para aula de Desenvolvimento de APIs e Microsserviços.

Como usar Docker:
no terminal, dentro da pasta escolaMaster, dê os seguintes comandos:
>> docker build -t nome-da-imagem .
>> docker run nome-da-imagem
Resultado esperado: 
O docker irá criar um ambiente e instalar todos os requerimentos, depois vai lançar o servidor Flask e fazer os testes instantaneamente.
É possível acompanhar todo esse procedimento pelo terminal.

JSON das entidades:

PROFESSOR - 
    {
        "data_nascimento": "1995-05-16",
        "disciplina": "API e Microsserviços",
        "nome": "Caio Ireno",
        "salario": "4582.00"
    }

TURMA - 
    {
        "nome": "API e Microsserviços",
        "professor_id": 1,
        "turno": "Noturno"
    }

ALUNO - 
    {
        "data_nascimento": "2002-04-12",
        "nome": "Mikael",
        "nota_primeiro_semestre": "9.00",
        "nota_segundo_semestre": "10.00",
        "turma_id": 1
    }

Necessário no requirements:

Requests==2.32.3
blinker==1.9.0
click==8.1.8
colorama==0.4.6
Flask==3.1.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
Werkzeug==3.1.3
SQLAlchemy==2.0.40
Flask-SQLAlchemy==3.1.1
flask-swagger-ui
flask-restx==1.1.0