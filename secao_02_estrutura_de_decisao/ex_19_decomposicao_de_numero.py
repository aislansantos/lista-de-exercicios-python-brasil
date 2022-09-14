"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    numeros = list()
    numero = numero
    caracteres = len(str(numero))
    if numero >= 1000:
        return(f'O número precisa ser menor que 1000')

    if numero < 0:
        return('O número precisa ser positivo')

    if numero > 0 and caracteres < 2:
        if numero == 1:
            return(f'1 = 1 unidade')
        return(f'{numero} = {numero} unidades')


    if caracteres == 2:
        for x in str(numero):
            numeros.append(x)
        if numeros[0] == '1':
            dezena = 'dezena'
        else:
            dezena = 'dezenas'
        if numeros[1] == '1':
            unidade = 'unidade'
        else:
            unidade = 'unidades'
        if numeros[1] != '0':
            return(f'{numero} = {numeros[0]} {dezena} e {numeros[1]} {unidade}')
        return(f'{numero} = {numeros[0]} {dezena}')

    if caracteres == 3:
        for x in str(numero):
            numeros.append(x)
        if numeros[0] == '1':
            centena = 'centena'
        else:
            centena = 'centenas'
        if numeros[1] == '1':
            dezena = 'dezena'
        else:
            dezena = 'dezenas'
        if numeros[2] == '1':
            unidade = 'unidade'
        else:
            unidade = 'unidades'
        if numeros[0] != '0' and numeros[1] != '0' and numeros[2] != '0':
            return(f'{numero} = {numeros[0]} {centena}, {numeros[1]} {dezena} e {numeros[2]} {unidade}')
        if numeros[2] == '0' and numeros[1] == '0':
            return(f'{numero} = {numeros[0]} {centena}')
        if numeros[1] != '0' and numeros[2] == '0':
            return(f'{numero} = {numeros[0]} {centena} e {numeros[1]} {dezena}')
        if numeros[1] == '0' and numeros[2] != '0':
            return(f'{numero} = {numeros[0]} {centena} e {numeros[2]} {unidade}')

