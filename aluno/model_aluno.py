from turma import model_turma
import datetime
from configuracao import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    nota_primeiro_semestre = db.Column(db.Numeric(10,2), nullable=False)
    nota_segundo_semestre = db.Column(db.Numeric(10,2), nullable=False)
    media_final = db.Column(db.Numeric(10,2), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

def lista_alunos():
    alunos = Aluno.query.all()
    lista = []
    for aluno in alunos:
        lista.append({
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final,
            "turma_id": aluno.turma_id
        })
    
    return lista


def aluno_by_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    try:
        estudante = {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final,
            "turma_id": aluno.turma_id
        }
        return estudante
    except:     
        return {"msg": "Aluno não encontrado", "erro": 400}


def post_alunos(dados):
    if "nome" not in dados:
        return {"msg":"Aluno sem nome.", "erro": 400}
    
    if empty(dados["turma_id"]):
        return {"msg":"Não há turmas, impossível criar alunos.", "erro": 400}
    
    if not "nota_primeiro_semestre" in dados or not "nota_segundo_semestre" in dados:
        return {"msg":"É necessário incluir as notas para adicionar um aluno.", "erro": 400}
    
    if not "data_nascimento" in dados:
        return {"msg":"Impossível registrar aluno sem Data de Nascimento.", "erro": 400}

    try: 
        dt_nascimento = dados["data_nascimento"]
        idade = calcula_idade(dt_nascimento)
        if idade < 17: return {"msg":"Erro: Alunos devem ter ao menos 17 anos.", "erro": 400}
        else: dados["idade"] = idade
            
    except:
       return {"msg":"Erro com a Data de Nascimento. Formato esperado: yyyy-MM-dd", "erro": 400}

    try:
        nota1 = float(dados["nota_primeiro_semestre"])
        nota2 = float(dados["nota_segundo_semestre"])
        media_calculada = media(nota1, nota2)
    except:
        return {"msg":"Erro com as notas. Catractere inválido.", "erro": 400}

    try:
        novo_aluno = Aluno(nome=dados["nome"], 
                           idade=dados["idade"], 
                           data_nascimento=dados["data_nascimento"], 
                           nota_primeiro_semestre=float(dados["nota_primeiro_semestre"]), 
                           nota_segundo_semestre=float(dados["nota_segundo_semestre"]), 
                           media_final=media_calculada,
                           turma_id=dados["turma_id"])
        
        db.session.add(novo_aluno)
        db.session.commit()
        return "Aluno adicionado com sucesso!"

    except:
        return {"msg":"Não foi possível aidicionar o Aluno", "erro": 500}


def put_Alunos(idAluno, resposta):
    aluno = Aluno.query.get(idAluno)
    chaves_necessarias = ["nome", "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre", "turma_id"]
    chaves_resposta = resposta.keys() 
    faltantes = []

    for item in chaves_necessarias:
        if item not in chaves_resposta:
            faltantes.append(item)

    if len(faltantes) > 0:
        return {"msg": f"É necessário preencher todos os campos. Faltantes: {faltantes}", "erro": 400}
    
    try: 
        dt_nascimento = resposta["data_nascimento"]
        idade = calcula_idade(dt_nascimento)
        if idade < 17: return {"msg":"Erro: Alunos devem ter ao menos 17 anos.", "erro": 400}
        else: resposta["idade"] = idade
       
    except:
       return {"msg":"Erro com a Data de Nascimento. Formato esperado: yyyy-MM-dd", "erro": 400}

    try:
        nota1 = float(resposta["nota_primeiro_semestre"])
        nota2 = float(resposta["nota_segundo_semestre"])
        media_calculada = media(nota1, nota2)
    except:
        return {"msg":"Erro com as notas. Catractere inválido.", "erro": 400}
    
    try:
        aluno.nome = resposta["nome"]
        aluno.idade = idade
        aluno.data_nascimento = resposta["data_nascimento"]
        aluno.nota_primeiro_semestre = float(resposta["nota_primeiro_semestre"])
        aluno.nota_segundo_semestre = float(resposta["nota_segundo_semestre"])
        aluno.media_final = media_calculada
        aluno.turma_id = resposta["turma_id"]
        
        db.session.commit()
        return "Alteração realizada com sucesso!"
    
    except:
        return {"msg":"Erro", "erro":400}


def delete_aluno(idAluno):
    try:
        aluno = Aluno.query.get(idAluno)     
        db.session.delete(aluno)
        db.session.commit()       
        return "Aluno deletado com sucesso!"
      
    except:
        return  {"msg":"Aluno não encontrado", "erro": 400}

def resetaAlunos():
    db.session.query(Aluno).delete()
    db.session.commit()
    return "Todos os alunos foram apagados."

def existe_aluno():
    alunos = Aluno.query.all()
    lista = []
    for aluno in alunos:
        objeto = {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "turma_id": aluno.turma_id
        }
        lista.append(objeto)
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


def empty(id):
    id = int(id)          
    turmas = model_turma.existe_turma()
    for turma in turmas:
        if turma['id'] == id:
            return False
    else:
        return True
