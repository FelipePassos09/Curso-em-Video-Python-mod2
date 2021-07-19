'''
Crie um programa que leia vários numeros inteiros pelo teclado. Ele só vai parar quando o usuário digitar 999, que a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles.

(desconsiderando a flag)
'''
tach = ('=='*20)
print(f'\033[31m{tach}\nTABUADA\n{tach}\033[m')

nmr = soma = cont = 0

while True:
    nmr = int(input('Diga um número: \n'))
    if nmr == 999:
        break
    soma += nmr
    cont += 1
print(f'Você digitou {cont} numeros.')
print(f'A soma entre esses números foi {soma}')