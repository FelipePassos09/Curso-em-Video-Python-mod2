# Desenvolva um programa que leia o primeiro e a razão de uma Progreção Aritimética (PA). No final 
# mostre os 10 primeiros termos dessa progreção.

pri = int(input('Diga onde começa sua PA: \n'))
r = int(input('Diga qual a razão da sua PA:\n'))

print('Os 10 primeiros itens da PA iniciando em {} e com razão {} são:\n'.format(pri, r))
for i in range(pri, r*11 , r):
    print('→ ',i, end = ' ')