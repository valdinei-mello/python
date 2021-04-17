"""
Sistemas de Arquivos - Navegação

Para fazer uso de manipulação de arquivos do SO, precisamos importar e faer uso do modulo os.

os = Operating System - Sistema Operacional

=======================================================

# Fazer o import
import os

# getpwd() = pega o current work directory - diretório de trabalho corrente
# retorno o path ( caminho) absoluto
print(os.getcwd())  # C:\\Users/Valdinei Mello\\Desktop\\Curso_de_python

# para mudar o doretorio, podemos usar o chdir()

os.chdir('..')
print(os.getcwd())  # C:\\Users\\Valdinei Mello\\Desktop

os.chdir('..')
print(os.getcwd())  # C:\\Users\\Valdinei Mello

os.chdir('..')
print(os.getcwd())  # C:\\Users

os.chdir('..')
print(os.getcwd())  # C:\\


===========================================

# Podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('C:\\Users\\Valdinei Mello\\Desktop\\Curso_de_python'))  # True

=====================================

# OBS para usuarios windows
# Se você, infelizmente, estiver utilizando um computador com windows, terá que ter cuidado ao verificar diretórios.

print(os.path.isabs(' C:\\Users'))

==============================


# Podemos identificar o sistema operacional com o modulo os
print(os.name)  # posix (Linux e Mac) NT (Windows)

# Podemos ter mais detelhes no sistema operacional (Linux)
print(os.uname())


"""

# Fazer o import
import os


