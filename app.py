from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

dicionario = {
    "Alunos": [
        {
            "id": 1,
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
    return jsonify("Aluno não encontrado!")


@app.route('/alunos', methods=["POST"])
def postAlunos():
    dados = request.json
    alunos = dicionario["Alunos"]

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
            if aluno['nome'] != resposta['nome']: aluno['nome'] = resposta['nome'] #Se for diferente muda, se não segue
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
    return jsonify("Id do aluno não encontrado")

@app.route('/alunos/<int:idAluno>', methods=["DELETE"])
def deleteAlunos(idAluno):
    alunos = dicionario["Alunos"]
    for aluno in alunos:                #percorre o Array Alunos 
        if aluno["id"] == idAluno:      #compara os IDs
            resposta = request.json     
            alunos.remove(aluno)        #Remore o objeto do array
            return jsonify(resposta)
    else:
        return jsonify("Aluno não encontrado...")

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
        return jsonify("Professor não encontrado.") #Senão, não!

@app.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    professores = dicionario["Professores"]

    dt_nascimento = dados["data_nascimento"] # Retorna a data de Nascimento fornecida
    idade = calcula_idade(dt_nascimento)     # Chama a função de Calcular Idade
    dados["idade"] = idade                   # Adiciona a chave 'Idade' junto com o valor retornado da função

    professores.append(dados)
    return jsonify(dados)

@app.route('/professores/<int:idProfessor>', methods=["DELETE"])
def deleteProfessores(idProfessor):
    professores = dicionario["Professores"]      #Resgata a lista de dicionarios professores
    for professor in professores:                #percorre o Array professores 
        if professor["id"] == idProfessor:      #compara os IDs
            resposta = request.json     
            professores.remove(professor)        #Remore o objeto do array
            return jsonify(resposta)
    else:
        return jsonify("Professor não encontrado...")

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

if __name__ == '__main__':
    app.run(debug=True)