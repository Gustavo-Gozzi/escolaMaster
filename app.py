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
            "id": 1,
            "nome": "Caio",
            "idade": 0,
            "data_nascimento": "2000-03-16",
            "disciplina": "API",
            "salario": 5000
        }
    ],
    "Turma": [
        {
            "id": 1,
            "nome": "API",
            "turno": "Noturno",
            "professor_id": 1
        },
        {
            "id": 2,
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

# Seção Alunos

@app.route('/alunos', methods=['GET'])
def getAlunos():
    dados = dicionario["Alunos"]
    return jsonify(dados)

@app.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunosbyID(idAluno):
    alunos = dicionario["Alunos"] #-> Array JSONs
    for aluno in alunos:
        if aluno["id"] == idAluno:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}),404


@app.route('/alunos', methods=["POST"])
def postAlunos():
    if empty("Turma"):
        return jsonify("Não há turmas criadas, impossível de registrar alunos.")
    dados = request.json
    alunos = dicionario["Alunos"]
    
    #Verifica se já tem um aluno na
    for aluno in alunos:
        if aluno["id"] == dados["id"]:
            return jsonify({"erro": "id já utilizada"}),400 

    if "nome" not in dados:
        return jsonify({"erro": "aluno sem nome"}),400 

    dt_nascimento = dados["data_nascimento"] # Retorna a data de Nascimento fornecida
    idade = calcula_idade(dt_nascimento)     # Chama a função de Calcular Idade
    dados["idade"] = idade                   # Adiciona a chave 'Idade' junto com o valor retornado da função

    nota1 = dados["nota_primeiro_semestre"]  #Retorna a primeira nota
    nota2 = dados["nota_segundo_semestre"]   #Retorna a segunda nota
    dados["media_final"] = media(nota1, nota2) #Atribui a chave 'media_final' o retorno da função

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
                aluno['nome'] = resposta['nome'] #Se for diferente muda, se não segue
            if aluno['data_nascimento'] != resposta['data_nascimento']:
                aluno['data_nascimento'] = resposta['data_nascimento']
                dt_nascimento = resposta["data_nascimento"] # Retorna a data de Nascimento fornecida
                idade = calcula_idade(dt_nascimento)     # Chama a função de Calcular Idade
                aluno["idade"] = idade                   # Adiciona a chave 'Idade' junto com o valor retornado da função
            if aluno['nota_primeiro_semestre'] != resposta["nota_primeiro_semestre"] or aluno['nota_segundo_semestre'] != resposta['nota_segundo_semestre']:
                aluno["nota_primeiro_semestre"] = resposta["nota_primeiro_semestre"]
                aluno["nota_segundo_semestre"] = resposta["nota_segundo_semestre"]
                nota1 = resposta["nota_primeiro_semestre"]  #Retorna a primeira nota
                nota2 = resposta["nota_segundo_semestre"]   #Retorna a segunda nota
                aluno["media_final"] = media(nota1, nota2) #Atribui a chave 'media_final' o retorno da função
            
            return jsonify(resposta)
    return jsonify({"erro": "Aluno não encontrado"}),404

@app.route('/alunos/<int:idAluno>', methods=["DELETE"])
def deleteAlunos(idAluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:                #percorre o Array Alunos 
        if aluno["id"] == idAluno:      #compara os IDs
            alunos.remove(aluno)        #Remore o objeto do array
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
    professores = dicionario["Professores"] #Adiciona o Array de professores a variavel
    for professor in professores:           #Percorre essa lista
        if professor["id"] == idProfessor:  #Se o ID escolhido estiver entre os IDs de professores então
            return jsonify(professor)       #Todo o objeto será retornado
    else:
        return jsonify({"erro": "Professor não encontrado"}),400

@app.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    professores = dicionario["Professores"]

    #Verifica se já tem um professor com o id
    for professor in professores: 
        if professor["id"] == dados["id"]:
            return jsonify({"erro": "id já utilizada"}),400 
    
    if "nome" not in dados:
        return jsonify({"erro": "professor sem nome"}),400 

    dt_nascimento = dados["data_nascimento"] # Retorna a data de Nascimento fornecida
    idade = calcula_idade(dt_nascimento)     # Chama a função de Calcular Idade
    dados["idade"] = idade                   # Adiciona a chave 'Idade' junto com o valor retornado da função

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
    professores = dicionario["Professores"]      #Resgata a lista de dicionarios professores
    for professor in professores:                #percorre o Array professores 
        if professor["id"] == idProfessor:      #compara os IDs
            professores.remove(professor)        #Remore o objeto do array
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
    return jsonify("Turma não encontrada!")

@app.route('/turmas', methods=["POST"])
def postTurmas():
    if empty("Professores"):
        return jsonify("Não é possível criar uma turma sem professores.")
    dados = request.json
    turma = dicionario["Turma"]
    
    turma.append(dados)
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
    return jsonify("Turma não encontrada...")

@app.route('/turmas/<int:idTurma>', methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = dicionario["Turma"]      #Resgata a lista de dicionarios turmas
    for turma in turmas:                #percorre o Array turmas 
        if turma["id"] == idTurma:      #compara os IDs
            turmas.remove(turma)        #Remore o objeto do array
            resposta = "Turma deletada com sucesso!"
            return jsonify(resposta)
    else:
        return jsonify("Turma não encontrada...")

#funcoes
def calcula_idade(data):   
    data = data.split("-")  #Transforma o dado recebido em lista usando '-' como separador
    ano = int(data[0])      #A lisa ficará assim: ["29", "07", "2003"]
    mes = int(data[1])      #Então cada variavel (ano, mes e dia) receberão seu valor exato de acordo
    dia = int(data[2])      #com o index
    data_nascimento = datetime.date(ano, mes, dia) #necessário importação da bibli 'datetime'
    hoje = datetime.date.today()
    idade = hoje - data_nascimento
    anos = idade.days // 365 #Pega o calculo de dias e divide por 365(1 ano)
    return anos

def media(nota1, nota2):
    soma = nota1 + nota2
    return soma / 2

def empty(texto):                       #Deve receber uma chave do nosso dicionario, ex: Turma
    texto = texto.capitalize()          #Garante que a string recebida tenha a primeira letra maiuscula
    if texto in dicionario:             #Verifica de a chave fornecida exite no dicionario.
        if len(dicionario[texto]) > 0:  #Caso a chave exista, verifica se ela possui algum dado salvo, "tamanho > 0"
            return False                #Se o tamanho da lista for maior que 0, então retorna falso "não está vazio"
        else:                           
            return True                 #Se for menor ou igual a zero, então a lista está vazia
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)