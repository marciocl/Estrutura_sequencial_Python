# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
# 11% para o Imposto de Renda,
#  8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valor_hora = float(input('Insira o valor das suas horas: '))
qt_horas = float(input('Insira a quantidade de horas que você trabalhou esse mês: '))

salario_bruto = valor_hora * qt_horas
inss = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
salario_Liquido = salario_bruto - inss - sindicato

print('Salário Bruto: R$ '+ str(salario_bruto))
print(('Desconto INSS: R$ ') + str(inss))
print(('Desconto sindicato: R$ ') + str(sindicato))
print(('Valor salario Liquido R$ ') + str(salario_Liquido))