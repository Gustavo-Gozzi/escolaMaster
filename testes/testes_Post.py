""" TESTES DO MÉTODO HTTP: POST de todas entidades """

import requests

def POST_professores(self):
    requests.post('http://localhost:8000/reseta')
    r = requests.post('http://localhost:8000/professores',json={
        "nome": "Gandalf",
        "data_nascimento": "1295-05-16",
        "disciplina": "Magia",
        "salario": 15000
    })
    r = requests.post('http://localhost:8000/professores',json={
        "nome": "Frodo",
        "data_nascimento": "1542-10-23",
        "disciplina": "Jornada",
        "salario": 4000
    })
    
    r_lista = requests.get('http://localhost:8000/professores')
    professores = r_lista.json()

    gandalf = False
    frodo = False
    for professor in professores:
        if professor['nome'] == 'Gandalf':
                gandalf = True
        if professor['nome'] == 'Frodo':
                frodo = True
        
    if not gandalf:
        self.fail('professor Gandalf nao encontrado.')
    if not frodo:
        self.fail('professor Frodo nao encontrado.')

def POST_turmas(self):
    r = requests.post('http://localhost:8000/turmas',json={
        "nome": "Magia",
        "turno": "Noturno",
        "professor_id": 1
    })
    r = requests.post('http://localhost:8000/turmas',json={
        "nome": "Jornada",
        "turno": "Noturno",
        "professor_id": 2
    })
    
    r_lista = requests.get('http://localhost:8000/turmas')
    turmas = r_lista.json()

    magia = False
    jornada = False
    for turma in turmas:
        if turma['nome'] == 'Jornada':
            jornada = True
        if turma['nome'] == 'Magia':
            magia = True
    
    if not jornada:
        self.fail('materia Jornada nao encontrada.')
    if not magia:
        self.fail('materia Magia nao encontrada.')

def POST_alunos(self):
    r = requests.post('http://localhost:8000/alunos',json={
        "nome": "Joao",
        "data_nascimento": "2004-08-29",
        "nota_primeiro_semestre": 8,
        "nota_segundo_semestre": 9,
        "turma_id": 1
    })
    r = requests.post('http://localhost:8000/alunos',json={
        "nome": "Mikael",
        "data_nascimento": "2002-04-12",
        "nota_primeiro_semestre": 7,
        "nota_segundo_semestre": 10,
        "turma_id": 2
    })
    
    r_lista = requests.get('http://localhost:8000/alunos')
    alunos = r_lista.json()

    joao = False
    mikael = False
    for aluno in alunos:
        if aluno['nome'] == 'Joao':
            joao = True
        if aluno['nome'] == 'Mikael':
            mikael = True
    
    if not joao:
        self.fail('aluno Joao nao encontrado.')
    if not mikael:
        self.fail('aluno Mikael nao encontrado.')

def POST_aluno_sem_turma(self):
    requests.post('http://localhost:8000/reseta/alunos')
    requests.post('http://localhost:8000/professores',json={
        "nome": "Ireno",
        "data_nascimento": "1999-11-21",
        "disciplina": "Farm em Tibia",
        "salario": 2200
    })
    requests.post('http://localhost:8000/turmas',json={
        "nome": "Farm",
        "turno": "Noturno",
        "professor_id": 1
    })
    

    r = requests.post('http://localhost:8000/alunos',json={
        "nome": "Joao",
        "data_nascimento": "2004-08-29",
        "nota_primeiro_semestre": 8,
        "nota_segundo_semestre": 9,
        "turma_id": 1
    })
    self.assertEqual(r.status_code,200)

    r = requests.post('http://localhost:8000/alunos',json={
        "nome": "Mikael",
        "data_nascimento": "2002-04-12",
        "nota_primeiro_semestre": 7,
        "nota_segundo_semestre": 10,
        "turma_id": 1000
    })
    self.assertEqual(r.status_code,400)

    r_lista = requests.get('http://localhost:8000/alunos')
    alunos = r_lista.json()

    joao = False
    mikael = False
    for aluno in alunos:
        if aluno['nome'] == 'Joao':
            joao = True
        if aluno['nome'] == 'Mikael':
            mikael = True
    
    if not joao:
        self.fail('aluno Joao nao encontrado.')
    if mikael:
        self.fail('aluno Mikael foi criado sem uma turma existente.')

def POST_turma_sem_professor(self):
    requests.post('http://localhost:8000/reseta/turma')
    requests.post('http://localhost:8000/reseta/professores')

    requests.post('http://localhost:8000/professores',json={
        "nome": "Ireno",
        "data_nascimento": "1999-11-21",
        "disciplina": "Farm em Tibia",
        "salario": 2200
    })

    r = requests.post('http://localhost:8000/turmas',json={
        "nome": "API",
        "turno": "Noturno",
        "professor_id": 1
    })
    
    self.assertEqual(r.status_code,200)

    r = requests.post('http://localhost:8000/turmas',json={
        "id": 2,
        "nome": "Mobile",
        "turno": "Noturno",
        "professor_id": 1987
    })
    
    self.assertEqual(r.status_code,400)

    r_lista = requests.get('http://localhost:8000/turmas')
    turmas = r_lista.json()

    api = False
    mobile = False
    for turma in turmas:
        if turma['nome'] == 'API':
            api = True
        if turma['nome'] == 'Mobile':
            mobile = True
    
    if not api:
        self.fail('materia API nao encontrada.')
    if mobile:
        self.fail('materia Mobile foi criada sem vinculo com professores.')

    requests.delete('http://localhost:8000/professores/1')