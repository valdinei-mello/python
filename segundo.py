import primeiro


def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('sefundo.py esta sendo executado diretamente')

else:
    print('segundo.py foi importado')