"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    from math import ceil, floor
    VALOR_LATA = 80
    VALOR_GALAO = 25

    area_a_ser_pintada = float(input('Area a ser pintada: '))
    litros_tinta_pintura = area_a_ser_pintada / 6
    litros_de_tinta_a_ser_usado = ceil((litros_tinta_pintura) + ((litros_tinta_pintura) * 10/100))
    print(f'Você deve comprar {litros_de_tinta_a_ser_usado} litros de tinta.')

    # Usando Latas
    latas_de_tinta = ceil(litros_de_tinta_a_ser_usado / 18)
    valor_latas_tinta = latas_de_tinta * VALOR_LATA
    litros_a_sobrar_lata = (latas_de_tinta * 18) - litros_de_tinta_a_ser_usado
    print(f'Você pode comprar {latas_de_tinta} lata(s) de 18 litros a um custo de R$ {valor_latas_tinta}. Vão sobrar {litros_a_sobrar_lata:.1f} litro(s) de tinta.')

    # Usando Galões
    galoes_de_tinta = ceil(litros_de_tinta_a_ser_usado / 3.6)
    valor_galoes_tinta = galoes_de_tinta * VALOR_GALAO
    litros_a_sobrar_galao = (galoes_de_tinta * 3.6) - litros_de_tinta_a_ser_usado
    print(f'Você pode comprar {galoes_de_tinta} lata(s) de 3.6 litros a um custo de R$ {valor_galoes_tinta}. Vão sobrar {litros_a_sobrar_galao:.1f} litro(s) de tinta.')

    # Usando Latas e Galões para melhorar os gastos
    latas_de_tinta = floor(litros_de_tinta_a_ser_usado)//18
    litros_faltantes = litros_de_tinta_a_ser_usado - (latas_de_tinta * 18)
    galoes_de_tinta = ceil(litros_faltantes / 3.6)
    valor_latas_tinta = latas_de_tinta * VALOR_LATA
    valor_galoes_tinta = galoes_de_tinta * VALOR_GALAO
    valor_total_tintas = valor_latas_tinta + valor_galoes_tinta
    sobra_tinta = 3.6 - litros_faltantes
    print(f'Para menor custo, você pode comprar {latas_de_tinta} lata(s) de 18 litros e {galoes_de_tinta} galão(ões) de 3.6 litros a um custo de R$ {valor_total_tintas}. Vão sobrar {sobra_tinta} litro(s) de tinta.')

    
