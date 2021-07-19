'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

tach = ('=='*20)
print(f'\033[33m{tach}\nCALCULADORA DE TABUADA\n{tach}\033[m')

num = int(input('Digite o número que deseja multiplicar: \n'))
c = 0

while num > 0:
    while c <= 10:
        print(f'{c} x {num} = {c*num}')
        c += 1
    num = int(input('Digite o número que deseja multiplicar: \n'))
    c = 0
print('FIM')
