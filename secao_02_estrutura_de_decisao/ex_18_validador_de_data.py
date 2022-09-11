"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""
from datetime import date, datetime


def validar_data(data: str):
    data = data
    if len(data) > 10 or len(data) < 8:
        return 'Data inválida'
    data = data.split('/')
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    dias_31 = [1,3,5,7,8,10,12]
    if mes < 1 or mes > 12:
        return 'Data inválida'
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            ultimo_dia = 29
            if dia > ultimo_dia:
                return 'Data inválida'
        else:
            ultimo_dia = 28
            if dia > ultimo_dia:
                return 'Data inválida'
    else:
        if mes in dias_31:
            ultimo_dia = 31
            if dia > ultimo_dia:
                return 'Data inválida'
        else:
            ultimo_dia = 30
            if dia > ultimo_dia:
                return 'Data inválida'

    return 'Data válida'

