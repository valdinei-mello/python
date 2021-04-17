"""
POO - Métodos Mágicos

Métodos magicos são todos os métodos que utilizam dunder.

    - def __init__(self, titulo, autor, paginas):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas

    - def __repr__(self):  # dunder repr: Retorna a representação do objeto
        return self.titulo

    - def __str__(self): # dudnder str: Retorna a representação do objeto, por ele tem maior prioridad em relação ao repr
        return self.titul

"""


class Livros:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # dunder repr: Retorna a representação do objeto
        return self.titulo

    def __str__(self):  # dudnder str: Retorna a representação do objeto, por ele tem maior prioridad em relação ao repr
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'Um objeto do tipo livro foi deletado')

    def __add__(self, other):
        return f'{self} - {other}'


livro1 = Livros('Python', 'Udemy', 421)
livro2 = Livros('Java', 'Fatec', 587)

print(livro1)
print(livro2)
print(len(livro1))

print(livro1 + livro2)

