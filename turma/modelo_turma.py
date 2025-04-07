from professor.model_professor import existe_professor
import datetime
#from funcoes import empty

dicionario = {
    "Turma": [
        {
            "id": 100,
            "nome": "API",
            "turno": "Noturno",
            "professor_id": 1
        },
        {
            "id": 200,
            "nome": "MOBILE",
            "turno": "Noturno",
            "professor_id": 2
        }
    ],
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
    professores = existe_professor()
    if empty("Professores", professor):
        return "Não é possível criar uma turma sem professores."

    turmas = dicionario["Turma"]
    
    try:
        professor_existe = False
        for professor in professores["Professores"]:
            if professor["id"] == dados["professor_id"]:
                professor_existe = True
                break  
        
        if not professor_existe:
            raise ValueError("Impossível criar turma sem um professor")

    except ValueError as e:
        return str(e)
    
    for turma in turmas:
        if turma["id"] == dados["id"]:
            return "id já utilizada"
        
    turmas.append(dados)

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
            resposta = "Turma deletada com sucesso!"
            return "Turma deletada com sucesso!"
        else:
            return "Turma não encontrada"

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