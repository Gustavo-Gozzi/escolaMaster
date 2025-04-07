from aluno import model_aluno
from turma import model_turma
from professor import model_professor

def reseta_all():
    alunos = model_aluno.existe_aluno()
    professores = model_professor.existe_professor()
    turmas = model_turma.existe_turma()
    
    alunos["Alunos"].clear()
    turmas["Turmas"].clear()
    professores["Professores"].clear()
    
    return "Tudo foi apagado."