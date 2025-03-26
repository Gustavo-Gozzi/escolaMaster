import datetime
dicionario = {
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
}

def lista_alunos():
    alunos = dicionario["Alunos"]
    return alunos

def aluno_by_id(id_aluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            return aluno
    else:
        return "Aluno não encontrado."
    
def post_alunos(dados):
    #if empty("Turma"):
        #return "Não há turmas criadas, impossível de registrar alunos.",400 ver depois
    if not "nota_primeiro_semestre" in dados or not "nota_segundo_semestre" in dados:
        return "É necessário incluir as notas para adicionar um aluno.",400
    alunos = dicionario["Alunos"]
    #turmas = dicionario["Turma"] ver depois
    if not "data_nascimento" in dados:
        return "Impossível registrar aluno sem Data de Nascimento.",400
    if not "nota_primeiro_semestre" in dados or not "nota_segundo_semestre" in dados:
        return "É necessário incluir as notas para adicionar um aluno.",400
    '''try:
        turma_existe = False

        for turma in turmas:
            if turma["id"] == dados["turma_id"]:
                turma_existe = True
                break  
        
        if not turma_existe:
            raise ValueError("Impossível criar aluno sem uma turma existente")

    except ValueError as e:
        return "erro"
''' #ver depois
    for aluno in alunos:
        if aluno["id"] == dados["id"]:
            return "erro: id já utilizada",400 

    if "nome" not in dados:
        return "erro: aluno sem nome",400 

    dt_nascimento = dados["data_nascimento"] 
    idade = calcula_idade(dt_nascimento)     
    dados["idade"] = idade                  
    nota1 = dados["nota_primeiro_semestre"]  
    nota2 = dados["nota_segundo_semestre"]   
    dados["media_final"] = media(nota1, nota2) 

    alunos.append(dados)
    return "Aluno adicionado com sucesso"


    #funções
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

def empty(texto):                       
    texto = texto.capitalize()          
    if texto in dicionario:             
        if len(dicionario[texto]) > 0:  
            return False                
        else:                           
            return True                 
    else:
        return False