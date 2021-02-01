# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('digite outro numero inteiro: '))
n3 = float(input('digite outro numero, mas agora real'))


dobro = (n1 * 2) + (n2 / 2)
soma_Triplo = (n2 * 3) + n3
ao_Cubo = n3 * n3 * n3

print (dobro)
print (soma_Triplo)
print (ao_Cubo)
