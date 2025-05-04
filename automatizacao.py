import subprocess
import os
from time import sleep

def encontrar_pasta():
    return os.path.dirname(os.path.abspath(__file__))

def rodar_tudo():
    pasta = encontrar_pasta()
    app_path = os.path.join(pasta, 'app.py')
    testes_path = os.path.join(pasta, 'testes', 'testesApp.py')
    servidor = subprocess.Popen(['python', app_path])
    sleep(3) 
    subprocess.run(['python', testes_path])
    servidor.terminate()

if __name__ == '__main__':
    rodar_tudo()
