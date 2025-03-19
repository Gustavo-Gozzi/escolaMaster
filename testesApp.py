import requests
import unittest

class TestStringMethods(unittest.TestCase):
    #Testango GET
    def test_001_GET_alunos(self):
        r = requests.get('http://localhost:5000/alunos')

        if r.status_code == 404:
            self.fail("Não existe a página Alunos.")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Não foi possível transformar em dicionario")

        self.assertEqual(type(obj_retornado),type([]))

    def test_002_GET_professores(self):
        r = requests.get('http://localhost:5000/professores')
        if r.status_code == 404:
            self.fail("Não existe a página Professores.")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Não foi possível transformar em dicionario")

        self.assertEqual(type(obj_retornado),type([]))

    def test_003_GET_turmas(self):
        r = requests.get('http://localhost:5000/turmas')
        if r.status_code == 404:
            self.fail("Não existe a página Turmas.")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Não foi possível transformar em dicionario")

        self.assertEqual(type(obj_retornado),type([]))

    #Testando POST
    def test_004_POST_alunos(self):
        r = requests.post('http://localhost:5000/alunos',json={
            "id": 1,
            "nome": "Joao",
            "idade": 0,
            "data_nascimento": "2004-08-29",
            "nota_primeiro_semestre": 8,
            "nota_segundo_semestre": 9,
            "turma_id": 0
        })
        r = requests.post('http://localhost:5000/alunos',json={
            "id": 2,
            "nome": "Mikael",
            "idade": 0,
            "data_nascimento": "2002-04-12",
            "nota_primeiro_semestre": 7,
            "nota_segundo_semestre": 10,
            "turma_id": 0
        })
        
        r_lista = requests.get('http://localhost:5000/alunos')
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

    def test_005_POST_professores(self):
        r = requests.post('http://localhost:5000/professores',json={
            "id": 1,
            "nome": "Caio",
            "idade": 0,
            "data_nascimento": "2000-03-16",
            "disciplina": "API",
            "salario": 5000
        })
        r = requests.post('http://localhost:5000/professores',json={
            "id": 2,
            "nome": "Frodo",
            "idade": 0,
            "data_nascimento": "1968-09-22",
            "disciplina": "Magia de Mordor",
            "salario": 4000
        })
        
        r_lista = requests.get('http://localhost:5000/professores')
        professores = r_lista.json()

        caio = False
        frodo = False
        for professor in professores:
            if professor['nome'] == 'Caio':
                caio = True
            if professor['nome'] == 'Frodo':
                frodo = True
        
        if not caio:
            self.fail('professor Caio nao encontrado.')
        if not frodo:
            self.fail('professor Frodo nao encontrado.')

    def test_006_POST_turmas(self):
        r = requests.post('http://localhost:5000/turmas',json={
            "id": 1,
            "nome": "API",
            "turno": "Noturno",
            "professor_id": 1
        })
        r = requests.post('http://localhost:5000/turmas',json={
            "id": 2,
            "nome": "Mobile",
            "turno": "Noturno",
            "professor_id": 2
        })
        
        r_lista = requests.get('http://localhost:5000/turmas')
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
        if not mobile:
            self.fail('materia Mobile nao encontrada.')
    
    #Testando GETs by ID
    def test_007_GETbyID_alunos(self):

        r = requests.post('http://localhost:5000/alunos',json={
            "id": 3,
            "nome": "Daniel",
            "idade": 0,
            "data_nascimento": "1995-03-27",
            "nota_primeiro_semestre": 5,
            "nota_segundo_semestre": 5,
            "turma_id": 0
        })

        resposta = requests.get('http://localhost:5000/alunos/3')
        dict_retornado = resposta.json()

        self.assertEqual(type(dict_retornado), dict)

        self.assertIn('nome',dict_retornado)

        self.assertEqual(dict_retornado['nome'],'Daniel') 

    def test_008_GETbyID_professores(self):

        r = requests.post('http://localhost:5000/professores',json={
            "id": 3,
            "nome": "Gandalf",
            "idade": 0,
            "data_nascimento": "1200-01-01",
            "disciplina": "Ressucitação",
            "salario": 10000
        })

        resposta = requests.get('http://localhost:5000/professores/3')
        dict_retornado = resposta.json()

        self.assertEqual(type(dict_retornado), dict)

        self.assertIn('nome',dict_retornado)

        self.assertEqual(dict_retornado['nome'],'Gandalf')

    def test_009_GETbyID_turmas(self):

        r = requests.post('http://localhost:5000/turmas',json={
            "id": 3,
            "nome": "Ressucitação",
            "turno": "Noturno",
            "professor_id": 3
        })

        resposta = requests.get('http://localhost:5000/turmas/3')
        dict_retornado = resposta.json()

        self.assertEqual(type(dict_retornado), dict)

        self.assertIn('nome',dict_retornado)

        self.assertEqual(dict_retornado['nome'],'Ressucitação') 

    #Testando DELETE
    def test_010_DELETE_alunos(self):
        requests.post('http://localhost:5000/alunos',json={
            "id": 4,
            "nome": "Luigi",
            "idade": 0,
            "data_nascimento": "1991-10-11",
            "nota_primeiro_semestre": 5,
            "nota_segundo_semestre": 5,
            "turma_id": 0
        })
        requests.delete('http://localhost:5000/alunos/4')
        r_get = requests.get('http://localhost:5000/alunos')
        alunos = r_get.json()
        for aluno in alunos:
            if aluno["nome"] == "Luigi":
                self.fail(f"O aluno {aluno['nome']} não foi deletado.")

    def test_011_DELETE_professores(self):
        requests.post('http://localhost:5000/professores',json={
            "id": 4,
            "nome": "Ireno",
            "idade": 0,
            "data_nascimento": "1999-11-21",
            "disciplina": "Farm em Tibia",
            "salario": 2200
        })
        requests.delete('http://localhost:5000/professores/4')
        r_get = requests.get('http://localhost:5000/professores')
        professores = r_get.json()
        for professor in professores:
            if professor["nome"] == "Ireno":
                self.fail(f"O professor {professor['nome']} não foi deletado.")    
    
    def test_012_DELETE_turmas(self):
        requests.post('http://localhost:5000/turmas',json={
            "id": 4,
            "nome": "Farm",
            "turno": "Noturno",
            "professor_id": 4
        })
        requests.delete('http://localhost:5000/turmas/4')
        r_get = requests.get('http://localhost:5000/turmas')
        turmas = r_get.json()
        for turma in turmas:
            if turma["nome"] == "Farm":
                self.fail(f"A turma {turma['nome']} não foi deletada.")   
    



  

    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()