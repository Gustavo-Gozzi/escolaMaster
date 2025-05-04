import requests
import unittest
import testes_Post, testes_Get, testes_Delete, testes_Put

class TestStringMethods(unittest.TestCase):
    
    #Testando POST
    def test_001_POST_professores(self):
        testes_Post.POST_professores(self)

    def test_002_POST_turmas(self):
        testes_Post.POST_turmas(self)

    def test_003_POST_alunos(self):
        testes_Post.POST_alunos(self)

    #Testando GET
    def test_004_GET_alunos(self):
        testes_Get.GET_alunos(self)

    def test_005_GET_professores(self):
        testes_Get.GET_professores(self)

    def test_006_GET_turmas(self):
        testes_Get.GET_turmas(self)

    #Testando GET by ID
    def test_007_GETbyID_professores(self):
        testes_Get.GETbyID_professores(self)

    def test_008_GETbyID_turmas(self):
        testes_Get.GETbyID_turmas(self)

    def test_009_GETbyID_alunos(self):
        testes_Get.GETbyID_alunos(self)

    #Testando DELETE
    def test_010_DELETE_professores(self):
        testes_Delete.DELETE_professor(self)

    def test_011_DELETE_turmas(self):
        testes_Delete.DELETE_turmas(self)            

    def test_012_DELETE_alunos(self):
        testes_Delete.DELETE_alunos(self)

    def test_013_POST_Aluno_SemTurma(self):
        testes_Post.POST_aluno_sem_turma(self)

    def test_014_POST_Turma_SemProfessor(self):
        testes_Post.POST_turma_sem_professor(self)    

    def test_015_PUT_professores(self):
        testes_Put.PUT_professores(self)

    def test_016_PUT_turma(self):
        testes_Put.PUT_turmas(self)

    def test_017_PUT_alunos(self):
        testes_Put.PUT_alunos(self)
    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()