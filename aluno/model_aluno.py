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


############### ALUNOS ########################
def lista_alunos():
    alunos = Aluno.query.all()
    lista = []
    for aluno in alunos:
        lista.append({
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "turma_id": aluno.turma_id
        })
    
    return lista


def aluno_by_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    try:
        estudante = {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "turma_id": aluno.turma_id
        }
        return estudante
    except:     
        return {"msg": "Aluno não encontrado", "erro": 400}


def post_alunos(dados):

    if "nome" not in dados:
        return {"msg":"Aluno sem nome.", "erro": 400}
    
    if empty(dados["turma_id"]):
        return {"msg":"Não há turmas, impossível criar alunos.", "erro": 400}
    
    if not "nota_primeiro_semestre" in dados or not "nota_segundo_semestre" in dados:
        return {"msg":"É necessário incluir as notas para adicionar um aluno.", "erro": 400}
    
    if not "data_nascimento" in dados:
        return {"msg":"Impossível registrar aluno sem Data de Nascimento.", "erro": 400}
    
    dt_nascimento = dados["data_nascimento"]
    idade = calcula_idade(dt_nascimento)
    dados["idade"] = idade
    nota1 = dados["nota_primeiro_semestre"]
    nota2 = dados["nota_segundo_semestre"]
    dados["media_final"] = media(nota1, nota2)

    try:
        novo_aluno = Aluno(nome=dados["nome"], idade=dados["idade"], data_nascimento=dados["data_nascimento"], nota_primeiro_semestre=dados["nota_primeiro_semestre"], nota_segundo_semestre=dados["nota_segundo_semestre"], turma_id=dados["turma_id"])
        db.session.add(novo_aluno)
        db.session.commit()
        return "Aluno adicionado com sucesso!"

    except:
        return {"msg":"Não foi possível aidicionar o Aluno", "erro": 500}


def put_Alunos(idAluno, resposta):
    aluno = Aluno.query.get(idAluno)
    chaves_necessarias = ["nome", "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre", "turma_id"]
    chaves_resposta = resposta.keys() #[nome, idade, data_nascimento, nota_1, nota2, turma_id]
    faltantes = []

    for item in chaves_necessarias:
        if item not in chaves_resposta:
            faltantes.append(item)

    if len(faltantes) > 0:
        return {"msg": f"É necessário preencher todos os campos. Faltantes: {faltantes}", "erro": 400}
    
    try:
        aluno.nome = resposta["nome"]
        aluno.idade = calcula_idade(resposta["data_nascimento"])
        aluno.data_nascimento = resposta["data_nascimento"]
        aluno.nota_primeiro_semestre = resposta["nota_primeiro_semestre"]
        aluno.nota_segundo_semestre = resposta["nota_segundo_semestre"]
        aluno.turma_id = resposta["turma_id"]
        
        db.session.commit()
        return "Alteração realizada com sucesso!"
    
    except:
        return {"msg":"Erro", "erro":400}


def delete_aluno(idAluno):
    try:
        aluno = Aluno.query.get(idAluno)     
        db.session.delete(aluno)
        db.session.commit()       
        return "Aluno deletado com sucesso!"
      
    except:
        return  {"msg":"Aluno não encontrado", "erro": 400}

def resetaAlunos():
    db.session.query(Aluno).delete()
    db.session.commit()
    return "Todos os alunos foram apagados."

#funcoes

def existe_aluno():
    alunos = Aluno.query.all()
    lista = []
    for aluno in alunos:
        objeto = {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "turma_id": aluno.turma_id
        }
        lista.append(objeto)
    return lista


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


def empty(id):
    print(id)                      
    id = int(id)          
    turmas = model_turma.existe_turma()
    for turma in turmas:
        if turma['id'] == id:
            return False
    else:
        return True
