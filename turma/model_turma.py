from professor import model_professor
import datetime
#from funcoes import empty


dicionario = {
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
}


###############TURMAS###################

def lista_turmas():
    turmas = dicionario["Turma"]
    return turmas

def turma_by_id(idTurma):
    turmas = dicionario["Turma"]
    
    for turma in turmas:
        if turma["id"] == idTurma:
            return turma
    else:
        return "Turma não encontrada"
        
def post_turma(dados):
    turmas = dicionario["Turma"]
    professor = model_professor.existe_professor()
    if empty("Professores", professor):
        return "Não há professores registrados, portanto é impossível criar turmas"

    try:
        professor_existe = False
        for professor in professor["Professores"]:
            if professor["id"] == dados["professor_id"]:
                professor_existe = True
                break  
        
        if not professor_existe:
            raise ValueError("É necessário ter um ID de professor válido")

    except ValueError as e:
        return str(e)
    
    for turma in turmas:
        if turma["id"] == dados["id"]:
            return "id já utilizada"
        
    turmas.append(dados)
    print(turmas)
    return "Turma adicionada com sucesso"


def put_turma(idTurma, resposta):
    turmas = dicionario["Turma"]
    for turma in turmas:
        if turma["id"] == idTurma:
            
            if turma["nome"] != resposta["nome"]:
                turma["nome"] = resposta["nome"]

            if turma["turno"] != resposta["turno"]:
                turma["turno"] = resposta["turno"]

            if turma["professor_id"] != resposta["professor_id"]:
                turma["professor_id"] = resposta["professor_id"]

            return "Alteração realizada com sucesso!"
    return "Turma não encontrada."

def deleteTurma(idTurma):
    turmas = dicionario["Turma"]      
    for turma in turmas:                
        if turma["id"] == idTurma:      
            turmas.remove(turma)        
            return "Turma deletada com sucesso!"
    else:
        return "Turma não encontrada"


def reseta_Turmas():
    dados = dicionario["Turma"]
    dicionario["Turma"].clear()
    return dados

# funcoes
def existe_turma():
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


def empty(texto, dicionario):                       
    texto = texto.capitalize()          
    if texto in dicionario:             
        if len(dicionario[texto]) > 0:  
            return False                
        else:                           
            return True                 
    else:
        return False