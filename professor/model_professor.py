#from funcoes import calcula_idade, empty
import datetime
from configuracao import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    disciplina = db.Column(db.String(200), nullable=False)
    salario = db.Column(db.Numeric(10,2), nullable=False)

    #relacao
    turma = db.relationship('Turma', backref='professor', lazy=True, cascade='all, delete-orphan')

def lista_professores():
    professores = Professor.query.all()
    lista = []
    for professor in professores:
        fessor = {
            "id": professor.id,
            "nome": professor.nome,
            "idade": professor.idade,
            "data_nascimento": professor.data_nascimento,
            "disciplina": professor.disciplina,
            "salario": professor.salario
        }
        lista.append(fessor)
    return lista


def professores_by_id(id_professor):
    professor = Professor.query.get(id_professor)
    try:
        fessor = {
            "id": professor.id,
            "nome": professor.nome,
            "idade": professor.idade,
            "data_nascimento": professor.data_nascimento,
            "disciplina": professor.disciplina,
            "salario": professor.salario
        }
        return fessor
    except:     
        return {"msg": "Professor não encontrado", "erro": 400}
    

def post_professor(dados):
    if not "data_nascimento" in dados:
        return  {"msg":"Impossível registrar professor sem Data de Nascimento.", "erro": 400}
    
    if "nome" not in dados:
        return  {"msg":"professor sem nome", "erro": 400}
    
    chaves_necessarias = ["nome", "data_nascimento", "disciplina", "salario"]
    chaves_resposta = dados.keys()
    faltantes = []

    for item in chaves_necessarias:
        if item not in chaves_resposta:
            faltantes.append(item)

    if len(faltantes) > 0:
        return {"msg": f"É necessário preencher todos os campos. Faltantes: {faltantes}", "erro": 400}

    try: 
        dt_nascimento = dados["data_nascimento"]
        age = calcula_idade(dt_nascimento)
        if age < 18: return {"msg":"Erro: Professores devem ter ao menos 18 anos.", "erro": 400}
        else: dados["idade"] = age
       
    except:
       return {"msg":"Erro com a Data de Nascimento. Formato esperado: yyyy-MM-dd", "erro": 400}    

    try:
        novo_professor = Professor(nome=dados["nome"], 
                                   idade=age, 
                                   data_nascimento=dt_nascimento, 
                                   disciplina=dados["disciplina"], 
                                   salario=dados["salario"])
        
        db.session.add(novo_professor)
        db.session.commit()
        return "Professor adicionado com sucesso!"

    except:
        return {"msg":"Não foi possível aidicionar professor", "erro": 500}
    

def put_professor(idProfessor, resposta):
    professor = Professor.query.get(idProfessor)
    chaves_necessarias = ["nome", "data_nascimento", "disciplina", "salario"]
    chaves_resposta = resposta.keys()
    faltantes = []

    for item in chaves_necessarias:
        if item not in chaves_resposta:
            faltantes.append(item)

    if len(faltantes) > 0:
        return {"msg": f"É necessário preencher todos os campos. Faltantes: {faltantes}", "erro": 400}  
    
    try: 
        dt_nascimento = resposta["data_nascimento"]
        age = calcula_idade(dt_nascimento)
        if age < 18: return {"msg":"Erro: Professores devem ter ao menos 18 anos.", "erro": 400}
        else: resposta["idade"] = age
       
    except:
       return {"msg":"Erro com a Data de Nascimento. Formato esperado: yyyy-MM-dd", "erro": 400}

    try:
        
        professor.nome = resposta["nome"]
        professor.data_nascimento = resposta["data_nascimento"]
        professor.disciplina = resposta["disciplina"]
        professor.salario = resposta["salario"]
        professor.idade = age

        db.session.commit()
        return "Alteração realizada com sucesso!"
        
    except:
        return  {"msg":"Professor não encontrado", "erro": 400}

def delete_professor(idProfessor):
    try:
        professor = Professor.query.get(idProfessor)     
        db.session.delete(professor)
        db.session.commit()       
        return "Professor deletado com sucesso!"
      
    except:
        return  {"msg":"Professor não encontrado", "erro": 400}

def reseta_Professores():
    db.session.query(Professor).delete()
    db.session.commit()
    return "Todos os professores foram apagados."

#funcoes
def existe_professor():
    professores = Professor.query.all()
    lista = []
    for professor in professores:
        fessor = {
            "id": professor.id,
            "nome": professor.nome,
            "idade": professor.idade,
            "data_nascimento": professor.data_nascimento,
            "disciplina": professor.disciplina,
            "salario": professor.salario
        }
        lista.append(fessor)
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

def empty(texto, dicionario):                       
    texto = texto.capitalize()          
    if texto in dicionario:             
        if len(dicionario[texto]) > 0:  
            return False                
        else:                           
            return True                 
    else:
        return False