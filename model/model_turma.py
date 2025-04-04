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

def turma_by_id():
    turmas = dicionario["Turma"]
    for turma in turmas:
        if turma["id"] == idTurma:
            return turma
        else:
            return "Turma não encontrada"
        
def post_turma():
    if empty("Professores"):
        return "Não é possível criar uma turma sem professores."

    turmas = dicionario["Turma"]
    professores = dicionario["Professores"]

    try:
        professor_existe = False
        for professor in professores:
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

def put_turma(idTurma):
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



def empty(texto):                       
    texto = texto.capitalize()          
    if texto in dicionario:             
        if len(dicionario[texto]) > 0:  
            return False                
        else:                           
            return True                 
    else:
        return False