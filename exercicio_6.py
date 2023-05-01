"""
Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada
"""

num = int(input('Digite um número: '))
print(f'O dobro do número {num} é igual a: {num * 2}')
print(f'O triplo do número {num} é igual a: {num * 3}')
print(f'A raiz quadrada do número {num} é igual a: {num ** (1/2):.2f}')