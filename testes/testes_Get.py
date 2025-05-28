""" TESTES DO MÉTODO HTTP: GET de todas entidades e o GET/ID """

import requests

def GET_alunos(self):
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

def GET_professores(self):
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

def GET_turmas(self):
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

def GETbyID_professores(self):
    requests.post('http://localhost:8000/reseta/professores')

    r = requests.post('http://localhost:8000/professores',json={
        "nome": "Gandalf",
        "idade": 0,
        "data_nascimento": "1200-01-01",
        "disciplina": "Ressucitação",
        "salario": 15000
    })

    resposta = requests.get('http://localhost:8000/professores/1')
    dict_retornado = resposta.json()

    self.assertEqual(type(dict_retornado), dict)

    self.assertIn('nome',dict_retornado)

    self.assertEqual(dict_retornado['nome'],'Gandalf')

def GETbyID_turmas(self):
    requests.post('http://localhost:8000/reseta/turmas')

    r = requests.post('http://localhost:8000/turmas',json={
        "nome": "Ressucitação",
        "turno": "Noturno",
        "professor_id": 1
    })

    resposta = requests.get('http://localhost:8000/turmas/1')
    dict_retornado = resposta.json()

    self.assertEqual(type(dict_retornado), dict)

    self.assertIn('nome',dict_retornado)

    self.assertEqual(dict_retornado['nome'],'Ressucitação')     

def GETbyID_alunos(self):
    requests.post('http://localhost:8000/reseta/alunos')

    r = requests.post('http://localhost:8000/alunos',json={
        "nome": "Daniel",
        "data_nascimento": "1995-03-27",
        "nota_primeiro_semestre": 5,
        "nota_segundo_semestre": 5,
        "turma_id": 1
    })

    resposta = requests.get('http://localhost:8000/alunos/1')
    dict_retornado = resposta.json()

    self.assertEqual(type(dict_retornado), dict)

    self.assertIn('nome',dict_retornado)

    self.assertEqual(dict_retornado['nome'],'Daniel') 
