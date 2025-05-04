""" TESTES DO MÉTODO HTTP: PUT de todas entidades """

import requests

def PUT_professores(self):
    requests.post('http://localhost:8000/reseta')
    
    r = requests.post('http://localhost:8000/professores',json={
        "nome": "Gandalf",
        "data_nascimento": "1295-05-16",
        "disciplina": "Magia",
        "salario": 15000
    })
    self.assertEqual(r.status_code, 200)

    r = requests.put('http://localhost:8000/professores/1', json={
        "nome": "Saruman",
        "data_nascimento": "1295-05-16",
        "disciplina": "Magia Negra",
        "salario": 20000
    })
    self.assertEqual(r.status_code, 200)

    r_lista = requests.get('http://localhost:8000/professores')
    professores = r_lista.json()

    gandalf = False
    saruman = False
    for professor in professores:
        if professor['nome'] == 'Gandalf':
                gandalf = True
        if professor['nome'] == 'Saruman':
                saruman = True
        
    if gandalf:
        self.fail('professor Gandalf encontrado, PUT não atualizou os dados.')
    if not saruman:
        self.fail('professor Saruman nao encontrado, PUT não atualizou os dados.')

def PUT_turmas(self):
    requests.post('http://localhost:8000/reseta/turmas')

    r = requests.post('http://localhost:8000/turmas',json={"nome": "Magia","turno": "Noturno","professor_id": 1})
    self.assertEqual(r.status_code, 200)

    r = requests.put('http://localhost:8000/turmas/1',json={"nome": "Jornada","turno": "Noturno","professor_id": 1})
    self.assertEqual(r.status_code, 200)

    r_lista = requests.get('http://localhost:8000/turmas')
    turmas = r_lista.json()

    magia = False
    jornada = False

    for turma in turmas:
        if turma['nome'] == 'Jornada':
            jornada = True
        if turma['nome'] == 'Magia':
            magia = True
    
    if magia:
        self.fail('materia Magia encontrada, PUT não atualizou os dados. ')
    if not jornada:
        self.fail('materia Jornada nao encontrada, PUT não atualizou os dados.')
    
def PUT_alunos(self):
    requests.post('http://localhost:8000/reseta/alunos')

    r = requests.post('http://localhost:8000/alunos',json={"nome": "Joao","data_nascimento": "2004-08-29","nota_primeiro_semestre": 8,"nota_segundo_semestre": 9,"turma_id": 1})
    self.assertEqual(r.status_code, 200)

    r = requests.put('http://localhost:8000/alunos/1',json={"nome": "Mikael","data_nascimento": "2002-04-12","nota_primeiro_semestre": 9,"nota_segundo_semestre": 10,"turma_id": 2})
    self.assertEqual(r.status_code, 200)

    r_lista = requests.get('http://localhost:8000/alunos')
    alunos = r_lista.json()

    joao = False
    mikael = False
    for aluno in alunos:
        if aluno['nome'] == 'Joao':
            joao = True
        if aluno['nome'] == 'Mikael':
            mikael = True
    
    if joao:
        self.fail('aluno Joao encontrado, PUT não atualizou os dados.')
    if not mikael:
        self.fail('aluno Mikael nao encontrado, PUT não atualizou os dados.')