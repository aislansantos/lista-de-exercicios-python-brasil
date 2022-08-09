"""
Exercício 11 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

    >>> calcular_aumento(100)
    Salário atual: R$ 100.00
    Aumento porcentual: 20%
    Valor do aumento: R$ 20.00
    Novo salário: R$ 120.00
    >>> calcular_aumento(300)
    Salário atual: R$ 300.00
    Aumento porcentual: 15%
    Valor do aumento: R$ 45.00
    Novo salário: R$ 345.00
    >>> calcular_aumento(800)
    Salário atual: R$ 800.00
    Aumento porcentual: 10%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 880.00
    >>> calcular_aumento(1600)
    Salário atual: R$ 1600.00
    Aumento porcentual: 5%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 1680.00

"""


def calcular_aumento(salario: float):
    salario = salario
    if salario <= 280:
      salario_novo = salario + ((salario*20)/100)
      valor_aumento = salario_novo - salario
      print(f'Salário atual: R$ {salario:.2f}\nAumento porcentual: 20%\nValor do aumento: R$ {valor_aumento:.2f}\nNovo salário: R$ {salario_novo:.2f}')
    elif salario > 280 and salario <= 700:
      salario_novo = salario + ((salario*15)/100)
      valor_aumento = salario_novo - salario
      print(f'Salário atual: R$ {salario:.2f}\nAumento porcentual: 15%\nValor do aumento: R$ {valor_aumento:.2f}\nNovo salário: R$ {salario_novo:.2f}')
    elif salario > 700 and salario <= 1500:
      salario_novo = salario + ((salario*10)/100)
      valor_aumento = salario_novo - salario
      print(f'Salário atual: R$ {salario:.2f}\nAumento porcentual: 10%\nValor do aumento: R$ {valor_aumento:.2f}\nNovo salário: R$ {salario_novo:.2f}')
    else:
      salario_novo = salario + ((salario*5)/100)
      valor_aumento = salario_novo - salario
      print(f'Salário atual: R$ {salario:.2f}\nAumento porcentual: 5%\nValor do aumento: R$ {valor_aumento:.2f}\nNovo salário: R$ {salario_novo:.2f}')