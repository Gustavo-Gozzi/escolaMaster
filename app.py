from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

dicionario = {
    "Alunos": [
        {
            "id": 1,
            "nome": "Joao",
            "idade": 0,
            "data_nascimento": "",
            "nota_primeiro_semestre": 0,
            "nota_segundo_semestre": 0,
            "turma_id": 0
        }
    ],
    "Professores": [
        {
            "id": 1,
            "nome": "Caio"
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
            aluno['nome'] = resposta['nome']
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

@app.route('/professores', methods=["POST"])
def postProfessores():
    dados = request.json
    alunos = dicionario["Professores"]
    alunos.append(dados)
    return jsonify(dados)


#funcoes
def calcula_idade(data):   
    data = data.split("/")  #Transforma o dado recebido em lista usando '/' como separador
    ano = int(data[2])      #A lisa ficará assim: ["29", "07", "2003"]
    mes = int(data[1])      #Então cada variavel (ano, mes e dia) receberão seu valor exato de acordo
    dia = int(data[0])      #com o index
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