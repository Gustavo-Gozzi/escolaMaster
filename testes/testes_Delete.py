""" TESTES DO MÉTODO HTTP: DELETE de todas entidades """

import requests

def DELETE_professor(self):
    requests.post('http://localhost:8000/reseta/professores')
    
    requests.post('http://localhost:8000/professores',json={
        "nome": "Ireno",
        "data_nascimento": "1999-11-21",
        "disciplina": "Farm em Tibia",
        "salario": 2200
    })
    requests.delete('http://localhost:8000/professores/1')
    r_get = requests.get('http://localhost:8000/professores')
    professores = r_get.json()
    for professor in professores:
        if professor["nome"] == "Ireno":
            self.fail(f"O professor {professor['nome']} não foi deletado.")

def DELETE_turmas(self):
    requests.post('http://localhost:8000/reseta/turmas')
    requests.post('http://localhost:8000/turmas',json={
        "nome": "Farm",
        "turno": "Noturno",
        "professor_id": 4
    })
    requests.delete('http://localhost:8000/turmas/1')
    r_get = requests.get('http://localhost:8000/turmas')
    turmas = r_get.json()
    for turma in turmas:
        if turma["nome"] == "Farm":
            self.fail(f"A turma {turma['nome']} não foi deletada.")

def DELETE_alunos(self):
    requests.post('http://localhost:8000/reseta/alunos')
    requests.post('http://localhost:8000/alunos',json={
        "nome": "Luigi",
        "idade": 0,
        "data_nascimento": "1991-10-11",
        "nota_primeiro_semestre": 5,
        "nota_segundo_semestre": 5,
        "turma_id": 1
    })
    requests.delete('http://localhost:8000/alunos/1')
    r_get = requests.get('http://localhost:8000/alunos')
    alunos = r_get.json()
    for aluno in alunos:
        if aluno["nome"] == "Luigi":
            self.fail(f"O aluno {aluno['nome']} não foi deletado.")