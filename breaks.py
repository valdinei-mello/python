"""
Saindo de loops com break

Funciona da mesma fomma que nas linguagens C ou JAVA.

Utilizamos os break para sair de loops de maneira projetada.
-----------------------------------------------------------
# Exemplo 1:

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("sai do loop")
------------------------------------------------------

"""




# Exemplo 2:

while True:
    comando = input("Digite sair para sair: ").upper()
    if comando == 'SAIR':
        print("Saindo...")
        break
