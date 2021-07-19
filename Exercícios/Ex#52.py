# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Diga um número:\n'))

p = 0
for i in range(1, num+1, 1):
    if (num % i ) == 0:
        print('\033[33m',end='') # Aplica cor para os números divisiveis.
        p += 1
    else:
        print('\033[34m', end='') # aplica outra cor para os não divisíveis.
    print('{}'.format(i), end = ' ')
# Checa quantidade de valores
if p == 2:
    print('\033[m\nO número {} É PRIMO.'.format(num))
else:
    print('\033[m\nO número {} NÃO É PRIMO.'.format(num))

print('Entre 2 e {}, esse número é divisivel {} vez(es).'.format(num, p))   
