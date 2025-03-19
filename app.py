from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

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
    "Professores": [
        {
            "id": 100,
            "nome": "Caio",
            "idade": 0,
            "data_nascimento": "2000-03-16",
            "disciplina": "API",
            "salario": 5000
        }
    ],
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
    ]
}


# Seção Reseta

@app.route('/reseta', methods=['POST'])
def reseta():
    dados = dicionario
    dicionario["Alunos"].clear()
    dicionario["Turma"].clear()
    dicionario["Professores"].clear()
    return jsonify(dados)
    
@app.route('/reseta/alunos', methods=['POST'])
def resetaAlunos():
    dados = dicionario["Alunos"]
    dicionario["Alunos"].clear()
    return jsonify(dados)

@app.route('/reseta/turmas', methods=['POST'])
def resetaTurmas():
    dados = dicionario["Turma"]
    dicionario["Turma"].clear()
    return jsonify(dados)

@app.route('/reseta/professores', methods=['POST'])
def resetaPRofessores():
    dados = dicionario["Professores"]
    dicionario["Professores"].clear()
    return jsonify(dados)

# Seção Alunos

@app.route('/alunos', methods=['GET'])
def getAlunos():
    dados = dicionario["Alunos"]
    return jsonify(dados)

@app.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunosbyID(idAluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}),404


@app.route('/alunos', methods=["POST"])
def postAlunos():
    if empty("Turma"):
        return jsonify("Não há turmas criadas, impossível de registrar alunos."),400
    dados = request.json
    alunos = dicionario["Alunos"]
    turmas = dicionario["Turma"]
    if not "data_nascimento" in dados:
        return jsonify("Impossível registrar aluno sem Data de Nascimento."),400
    try:
        turma_existe = False

        for turma in turmas:
            if turma["id"] == dados["turma_id"]:
                turma_existe = True
                break  
        
        if not turma_existe:
            raise ValueError("Impossível criar aluno sem uma turma existente")

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    for aluno in alunos:
        if aluno["id"] == dados["id"]:
            return jsonify({"erro": "id já utilizada"}),400 

    if "nome" not in dados:
        return jsonify({"erro": "aluno sem nome"}),400 

    dt_nascimento = dados["data_nascimento"] 
    idade = calcula_idade(dt_nascimento)     
    dados["idade"] = idade                  
    nota1 = dados["nota_primeiro_semestre"]  
    nota2 = dados["nota_segundo_semestre"]   
    dados["media_final"] = media(nota1, nota2) 

    alunos.append(dados)
    return jsonify(dados)

@app.route('/alunos/<int:idAluno>', methods=["PUT"])
def putAlunos(idAluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:
            resposta = request.json

            if "nome" not in resposta:
                    return jsonify({"erro": "aluno sem nome"}),400 

            if aluno['nome'] != resposta['nome']: 
                aluno['nome'] = resposta['nome'] 
            if aluno['data_nascimento'] != resposta['data_nascimento']:
                aluno['data_nascimento'] = resposta['data_nascimento']
                dt_nascimento = resposta["data_nascimento"] 
                idade = calcula_idade(dt_nascimento)     
                aluno["idade"] = idade                   
            if aluno['nota_primeiro_semestre'] != resposta["nota_primeiro_semestre"] or aluno['nota_segundo_semestre'] != resposta['nota_segundo_semestre']:
                aluno["nota_primeiro_semestre"] = resposta["nota_primeiro_semestre"]
                aluno["nota_segundo_semestre"] = resposta["nota_segundo_semestre"]
                nota1 = resposta["nota_primeiro_semestre"]  
                nota2 = resposta["nota_segundo_semestre"]   
                aluno["media_final"] = media(nota1, nota2) 
            
            return jsonify(resposta)
    return jsonify({"erro": "Aluno não encontrado"}),404

@app.route('/alunos/<int:idAluno>', methods=["DELETE"])
def deleteAlunos(idAluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos: 
        if aluno["id"] == idAluno:      
            alunos.remove(aluno)        
            return jsonify(aluno)
    else:
        return jsonify({"erro": "Aluno não encontrado"}),404

# Seção Professores

@app.route('/professores', methods=['GET'])
def getProfessores():
    dados = dicionario["Professores"]
    return jsonify(dados)

@app.route('/professores/<int:idProfessor>', methods=['GET'])
def getProfessoresByID(idProfessor):
    professores = dicionario["Professores"] 
    for professor in professores:           
        if professor["id"] == idProfessor:  
            return jsonify(professor)       
    else:
        return jsonify({"erro": "Professor não encontrado"}),400

@app.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    professores = dicionario["Professores"]
    if not "data_nascimento" in dados:
        return jsonify("Impossível registrar professor sem Data de Nascimento."),400

    for professor in professores: 
        if professor["id"] == dados["id"]:
            return jsonify({"erro": "id já utilizada"}),400 
    
    if "nome" not in dados:
        return jsonify({"erro": "professor sem nome"}),400 

    dt_nascimento = dados["data_nascimento"] 
    idade = calcula_idade(dt_nascimento)     
    dados["idade"] = idade                  

    professores.append(dados)
    return jsonify(dados)

@app.route('/professores/<int:idProfessor>', methods=['PUT'])
def putProfessores(idProfessor):
    professores = dicionario["Professores"]
    for professor in professores:
        if professor["id"] == idProfessor:
            resposta = request.json

            if "nome" not in resposta:
                return jsonify({"erro": "professor sem nome"}),400 

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
            return jsonify(resposta)
    return jsonify({"erro": "Professor não encontrado"}),400
            
@app.route('/professores/<int:idProfessor>', methods=["DELETE"])
def deleteProfessores(idProfessor):
    professores = dicionario["Professores"]      
    for professor in professores:                
        if professor["id"] == idProfessor:      
            professores.remove(professor)       
            resposta = "Professor deletado com sucesso!"
            return jsonify(resposta)
    else:
        return jsonify({"erro": "Professor não encontrado"}),400

# Seção de Turma:

@app.route('/turmas', methods=["GET"])
def getTurmas():
    turmas = dicionario["Turma"]
    return jsonify(turmas)

@app.route('/turmas/<int:idTurma>', methods=["GET"])
def getTurmasbyID(idTurma):
    turmas = dicionario["Turma"]
    for turma in turmas:
        if turma["id"] == idTurma:
            return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}),400

@app.route('/turmas', methods=["POST"])
def postTurmas():
    if empty("Professores"):
        return jsonify("Não é possível criar uma turma sem professores.")
    dados = request.json
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
        return jsonify({"erro": str(e)}), 400

    for turma in turmas:
        if turma["id"] == dados["id"]:
            return jsonify({"erro": "id já utilizada"}),400 

    turmas.append(dados)
    return jsonify(dados)

@app.route('/turmas/<int:idTurma>', methods=['PUT'])
def putTurma(idTurma):
    turmas = dicionario["Turma"]
    for turma in turmas:
        if turma["id"] == idTurma:
            resposta = request.json
            if turma["nome"] != resposta["nome"]:
                turma["nome"] = resposta["nome"]

            if turma["turno"] != resposta["turno"]:
                turma["turno"] = resposta["turno"]

            if turma["professor_id"] != resposta["professor_id"]:
                turma["professor_id"] = resposta["professor_id"]

            return jsonify(resposta)
    return jsonify({"erro": "Turma não encontrada"}),400

@app.route('/turmas/<int:idTurma>', methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = dicionario["Turma"]      
    for turma in turmas:                
        if turma["id"] == idTurma:      
            turmas.remove(turma)        
            resposta = "Turma deletada com sucesso!"
            return jsonify(resposta)
    else:
        return jsonify({"erro": "Turma não encontrada"}),400

#funcoes
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

if __name__ == '__main__':
    app.run(debug=True)