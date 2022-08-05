"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):
    n1 = x
    n2 = y
    n3 = z
    if n1 < n2 and n1  < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    elif n3 < n1 and n3 < n1:
        menor = n3

    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    elif n3 > n1 and n3 > n2:
        maior = n3
    
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
