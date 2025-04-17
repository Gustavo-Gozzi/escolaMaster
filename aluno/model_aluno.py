from turma import model_turma
import datetime
from configuracao import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    nota_primeiro_semestre = db.Column(db.Numeric(10,2), nullable=False)
    nota_segundo_semestre = db.Column(db.Numeric(10,2), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

'''dicionario = {
    "Alunos": [
        {
            "id": 100,
            "nome": "Joao",
            "idade": 0,
            "data_nascimento": "2004-08-29",
            "nota_primeiro_semestre": 0,
            "nota_segundo_semestre": 0,
            "turma_id": 0
        }
    ],
}'''


############### ALUNOS ########################
def lista_alunos():
    alunos = dicionario["Alunos"]
    return alunos


def aluno_by_id(id_aluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            return aluno
    else:
        return {"msg":"Aluno não encontrado!", "erro": 400}


def post_alunos(dados):
    turmas = model_turma.existe_turma()
    if empty("Turma", turmas):
        return "Não há turmas, impossível criar alunos."
    
    if not "nota_primeiro_semestre" in dados or not "nota_segundo_semestre" in dados:
        return {"msg":"É necessário incluir as notas para adicionar um aluno.", "erro": 400}
    
    alunos = dicionario["Alunos"]

    if not "data_nascimento" in dados:
        return {"msg":"Impossível registrar aluno sem Data de Nascimento.", "erro": 400}
    
    if not "nota_primeiro_semestre" in dados or not "nota_segundo_semestre" in dados:
        return {"msg":"É necessário incluir as notas para adicionar um aluno.", "erro": 400}
    try:
        turma_existe = False

        for turma in turmas["Turma"]:
            if turma["id"] == dados["turma_id"]:
                turma_existe = True
                break

        if not turma_existe:
            return {"msg":"Impossível criar aluno sem uma turma existente", "erro": 400}

    except ValueError as e:
        return "erro"

    for aluno in alunos:
        if aluno["id"] == dados["id"]:
            return {"msg":"erro: id já utilizada", "erro": 400}

    if "nome" not in dados:
        return {"msg":"Aluno sem nome.", "erro": 400}

    dt_nascimento = dados["data_nascimento"]
    idade = calcula_idade(dt_nascimento)
    dados["idade"] = idade
    nota1 = dados["nota_primeiro_semestre"]
    nota2 = dados["nota_segundo_semestre"]
    dados["media_final"] = media(nota1, nota2)

    alunos.append(dados)
    return "Aluno adicionado com sucesso"


def put_Alunos(idAluno, resposta):
    alunos = dicionario["Alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:

            if "nome" not in resposta:
                return {"msg":"Aluno sem nome.", "erro": 400}

            if aluno['nome'] != resposta['nome']:
                aluno['nome'] = resposta['nome']

            if aluno['data_nascimento'] != resposta['data_nascimento']:
                aluno['data_nascimento'] = resposta['data_nascimento']
                dt_nascimento = resposta["data_nascimento"]
                idade = calcula_idade(dt_nascimento)
                aluno["idade"] = idade

            if aluno['nota_primeiro_semestre'] != resposta["nota_primeiro_semestre"] or aluno[
                'nota_segundo_semestre'] != resposta['nota_segundo_semestre']:
                aluno["nota_primeiro_semestre"] = resposta["nota_primeiro_semestre"]
                aluno["nota_segundo_semestre"] = resposta["nota_segundo_semestre"]
                nota1 = resposta["nota_primeiro_semestre"]
                nota2 = resposta["nota_segundo_semestre"]
                aluno["media_final"] = media(nota1, nota2)

            return "Alteração realizada com sucesso!"


def delete_aluno(idAluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            alunos.remove(aluno)
            return "Aluno deletado com sucesso"
    else:
        return {"msg":"Aluno não encontrado!", "erro": 400}

def resetaAlunos():
    dados = dicionario["Alunos"]
    dicionario["Alunos"].clear()
    return dados

#funcoes

def existe_aluno():
    return dicionario


def calcula_idade(data):
    data = data.split("-")
    ano = int(data[0])
    mes = int(data[1])
    dia = int(data[2])
    data_nascimento = datetime.date(ano, mes, dia)
    hoje = datetime.date.today()
    idade = hoje - data_nascimento
    anos = idade.days // 365
    return anos


def media(nota1, nota2):
    soma = nota1 + nota2
    return soma / 2


def empty(texto, dicionario):
    texto = texto.capitalize()
    if texto in dicionario:
        if len(dicionario[texto]) > 0:
            return False
        else:
            return True
    else:
        return False
