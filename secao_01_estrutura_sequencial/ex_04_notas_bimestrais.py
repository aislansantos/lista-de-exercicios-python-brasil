"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    n1 = float(input('Digite uma nota:'))
    n2 = float(input('Digite uma nota:'))
    n3 = float(input('Digite uma nota:'))
    n4 = float(input('Digite uma nota:'))
    media = (n1+n2+n3+n4)/4
    print(f'A média anual é {media}')
