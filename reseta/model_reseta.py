from aluno import model_aluno
from turma import model_turma
from professor import model_professor
from configuracao import db

def reseta_all():
    alunos = model_aluno.Aluno.query.all()
    professores = model_professor.Professor.query.all()
    turmas = model_turma.Turma.query.all()
    
    try:
        for aluno in alunos:
            db.session.delete(aluno)
        
        for professor in professores:
            db.session.delete(professor)

        for turma in turmas:
            db.session.delete(turma)

        db.session.commit()
        return "Tudo foi apagado."
    
    except:
        return {"msg": "Algo deu errado...", "erro": 400}