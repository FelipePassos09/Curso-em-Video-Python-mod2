# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.


peso_mai = 0
peso_men = 0
for item in range(1,7,1):
    peso = float(input('Diga o peso da {}ª pessoa: \n'.format(item)))
    if item == 1:
        peso_mai = peso
        peso_men = peso
    else:
        if peso > peso_mai:
            peso_mai = peso
        if peso < peso_men:
            peso_men = peso
print('O maior peso foi {} e o menor foi {}.'.format(peso_mai, peso_men))