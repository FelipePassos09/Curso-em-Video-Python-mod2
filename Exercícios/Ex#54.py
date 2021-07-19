# Crie um programa que leia a data de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere a maioridade 21 anos.

from datetime import date

atual = date.today().year

maior = 0
menor = 0
for i in range(1,8,1):
    nasc = int(input('Ano de nascimento da {}ª pessoa:\n'.format(i)))
    if atual - nasc >= 21:
        maior += 1
    elif atual - nasc < 21:
        menor +=1
print('Dentre as informações passada apenas {} pessoas são maiores de idade.'.format(maior))
print('E {} pessoas são menores de idade.'.format(menor))



    