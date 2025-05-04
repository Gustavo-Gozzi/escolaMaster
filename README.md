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