from professor import model_professor
import datetime
from configuracao import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    turno = db.Column(db.String(200), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)

    #relacao
    aluno = db.relationship('Aluno', backref='turma', lazy=True)
#from funcoes import empty


'''dicionario = {
    "Turma": [
        {
            "id": 100,
            "nome": "DevOps",
            "professor_id": 101,
            "turno": "Diurno" 
        },
        {
            "id": 201,
            "nome": "APIS",
            "professor_id": 101,
            "turno": "Noturno"
        }
    ]
}'''


###############TURMAS###################

def lista_turmas():
    turmas = Turma.query.all()
    lista = []
    for turma in turmas:
        sala = {
            "id": turma.id,
            "nome": turma.nome,
            "professor_id": turma.professor_id,
            "turno": turma.turno
        }
        lista.append(sala)
    return lista

def turma_by_id(idTurma):
    turma = Turma.query.get(idTurma)

    try:
        sala = {
            "id": turma.id,
            "nome": turma.nome,
            "professor_id": turma.professor_id,
            "turno": turma.turno
        }
        return sala
    except:
        return  {"msg": "Turma não encontrada", "erro": 400}
        
        
def post_turma(dados):
    turmas = Turma.query.all()
    professores = model_professor.existe_professor()
    if empty(dados["professor_id"]):
        return  {"msg": "Não há professores registrados, portanto é impossível criar turmas", "erro": 400}
    

    try:
        professor_existe = False
        for professor in professores:
            if professor["id"] == dados["professor_id"]:
                professor_existe = True
                break  
        
        if not professor_existe:
            return{"msg":"É necessário ter um ID de professor válido", "erro": 400}

    except ValueError as e:
        return str(e)
    
    for turma in turmas:
        if turma.id == dados["id"]:
            return  {"msg": "id já utilizada", "erro": 400}
        
    try:
        nova_turma = Turma(nome=dados["nome"], professor_id=dados["professor_id"], turno=dados["turno"])
        db.session.add(nova_turma)
        db.session.commit()
        return "Turma adicionado com sucesso!"

    except:
        return {"msg":"Não foi possível aidicionar turma", "erro": 500}


def put_turma(idTurma, resposta):
    turma = Turma.query.get(idTurma)

    try:
        if turma.id == idTurma:
            
            if turma.nome != resposta["nome"]:
                turma.nome = resposta["nome"]

            if turma.turno != resposta["turno"]:
                turma.turno = resposta["turno"]

            if turma.professor_id != resposta["professor_id"]:
                turma.professor_id = resposta["professor_id"]
        
            db.session.commit()
            return "Alteração realizada com sucesso!"
    except: 
        return  {"msg": "Turma não encontrada.", "erro": 400}

def deleteTurma(idTurma):
    try:
        turma = Turma.query.get(idTurma)     
        db.session.delete(turma)
        db.session.commit()       
        return "Professor deletado com sucesso!"
      
    except:
        return  {"msg":"Professor não encontrado", "erro": 400}


def reseta_Turmas():
    turmas = Turma.query.all()
    for turma in turmas:
        db.session.delete(turma)
    db.session.commit
    return "Todas as turmas foram apagadas."

# funcoes
def existe_turma():
    turmas = Turma.query.all()
    lista = []
    for turma in turmas:
        sala = {
            "id": turma.id,
            "nome": turma.nome,
            "professor_id": turma.professor_id,
            "turno": turma.turno
        }
        lista.append(sala)
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


def empty(id):
    print(id)                      
    id = int(id)          
    professores = model_professor.existe_professor()
    for professor in professores:
        print(professor)
        if professor['id'] == id:
            return False
    else:
        return True