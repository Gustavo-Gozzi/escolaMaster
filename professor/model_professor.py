#from funcoes import calcula_idade, empty
import datetime

dicionario = {
    "Professores": [          #lista de dicionarios
        {
            "id": 100,
            "nome": "Caio",
            "idade": 0,
            "data_nascimento": "2000-03-16",
            "disciplina": "API",
            "salario": 5000
        },
        {
            "id": 101,
            "nome": "Odair",
            "idade": 100,
            "data_nascimento": "1925-03-16",
            "disciplina": "Mobile",
            "salario": 5000

        }
    ],
}

def lista_professores():
    professores = dicionario["Professores"] #-> professores [0, 1..]
    return professores


def professores_by_id(id_professor):
    professores = dicionario["Professores"] 
    for professor in professores:           
        if professor["id"] == id_professor:  
            return professor       
    else:
        return "Professor não encontrado"
    

def post_professor(dados):
    professores = dicionario["Professores"]
    if not "data_nascimento" in dados:
        return "Impossível registrar professor sem Data de Nascimento."

    for professor in professores: 
        if professor["id"] == dados["id"]:
            return "id já utilizada"
    
    if "nome" not in dados:
        return "professor sem nome"

    dt_nascimento = dados["data_nascimento"] 
    idade = calcula_idade(dt_nascimento)     
    dados["idade"] = idade                  

    professores.append(dados)
    return "Professor adicionado com sucesso!"

def put_professor(idProfessor, resposta):
    professores = dicionario["Professores"]
    for professor in professores:
        if professor["id"] == idProfessor:

            if "nome" not in resposta:
                return "professor sem nome"

            if professor['nome'] != resposta['nome']:
                professor['nome'] = resposta['nome']
            if professor['data_nascimento'] != resposta['data_nascimento']:
                professor['data_nascimento'] = resposta['data_nascimento']
                dt_nascimento = resposta["data_nascimento"] 
                idade = calcula_idade(dt_nascimento)
                professor["idade"] = idade
            if professor['disciplina'] != resposta['disciplina']:
                professor['disciplina'] = resposta['disciplina']
            if professor['salario'] != resposta['salario']:
                professor['salario'] = resposta['salario']
            return "Alteração realizada com sucesso!"
    return "Professor não encontrado"

def delete_professor(idProfessor):
    professores = dicionario["Professores"]      
    for professor in professores:                
        if professor["id"] == idProfessor:      
            professores.remove(professor)       
            return "Professor deletado com sucesso!"
             
    else:
        return "Professor não encontrado"


#funcoes
def existe_professor():
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