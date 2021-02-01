#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = str(input('Qual o seu sexo M or F ? '))

if sexo == "M":
    alturaM = float(input('Qual a sua altura moço '))

elif sexo == "F":
    alturaF = float(input('Qual a sua altura moça '))


if sexo == "M":
    print ((72.7*alturaM) - 58 )

elif sexo == "F":
    print ((62.1*alturaF) - 44.7)



