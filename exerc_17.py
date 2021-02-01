# Faça um Programa para uma loja de tintas. >Feito<
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. >Feito<
# Considere que a cobertura da tinta é de 1 litro para cada  6 metros quadrados >Feito<
# e que a tinta é vendida em latas de 18 litros, >Feito<
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. >Feito<
# Informe ao usuário as quantidades de tinta a serem compradas >Feito<
# e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias

# Problema 1: a Multiplicação lataP x preco P não esta exata. >Feito<
# Problema 2: a Multiplicação lataG x preco G não esta exata. >Feito<

metro = int(input('Quantos metros de parede você precisa pintar: '))

# Tamanho das Latas
lataG = 18
lataP = 3.60

# Preço das Latas
precoG = 80
precoP = 25

# essa varíavel calcula a quantidade de litros em relação a quantidade de metros a ser pintada.
litro = ((metro)/ 6 * 1.10)

# Latas 18 Litros
litro_lataG = litro / lataG


if (litro%lataG !=0):
    arrend_litro_lataG = (int(litro_lataG +1))
    print('Se for comprar latas de 18 litros você precisará de:',int(arrend_litro_lataG), 'galão(ões) e custará: R$ ', arrend_litro_lataG * precoG)
elif (litro%lataG == 0):
    print('Se for comprar latas de 18 litros você precisará de:',int(litro_lataG), 'galão(ões) e custará: R$ ', litro_lataG * precoP)

# Latas de 3.6

litro_lataP = litro / lataP

if (litro%lataP !=0):
    litro_lataP = int(litro_lataP +1)


elif (litro%lataG == 0):
    (litro_lataP) = int(litro_lataP)

print('Se for comprar latas de 3.6 litros você precisará de:',int(litro_lataP), 'galão(ões) e custará: R$ ', int(litro_lataP) * precoP,'.')


#evitando disperdício

# Valor evitando disperdício


# Estrutura de decisão para definir se o número é exato ou quebrado. 
x = ()

if (litro%lataG !=0):
    x = arrend_litro_lataG
elif (litro%lataG == 0):
    x = litro_lataG



# Estrutura de decisão que calcula quando deve comprar um galão menor para evitar o disperdício.
qtP = ()

if (100-(x - litro_lataG) * 100) >60.0:
    qtP = 0
elif (100-(x - litro_lataG) * 100 <60.0 and (x - litro_lataG) * 100) > 40.0:
    qtP = 1
elif (100-(x - litro_lataG) * 100 <40.0 and (x - litro_lataG) * 100) > 20.0:
    qtP = 2
elif (100-(x - litro_lataG) * 100 <20.0 and (x - litro_lataG) * 100) > 0:
    qtP = 3
elif (100-(x - litro_lataG) * 100)  <= 0:
    qtP = 0

#Melhor Valor

valor_sem_disperdicio = (qtP * precoP) + ( x * precoG)

if metro <65:
    print('Compre Galões menores')
elif (litro_lataG * precoG) < valor_sem_disperdicio:
    print('A maneira mais barata e eficiete é comprar ',int(litro_lataG), 'lata(s) de 18 litros e ', int(qtP), 'galão(ões) de 3.6', 'o valor total é de R$', ((int(litro_lataG)*precoG))+(qtP*precoP))
















