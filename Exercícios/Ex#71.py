'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$ 50, 20, 10 e 1.

'''
print('\033[33m=='*20)
print('CAIXA ELETRONICO PYTHON.')
print('=='*20,'\033[m')

val = int(input('\nInforme o valor a sacar: \n'))
ced50 = 0
ced20 = 0
ced5 = 0
ced1 = 0

print('\n')

while True:
    if val // 50 > 0:
        ced50 = val//50
        print(f'Voce receberá {ced50} cedulas de R$ 50,00.')
        val = val%50
    if val // 20 > 0:
        ced20 = val//20
        print(f'Receberá {ced20} cédulas de R$ 20,00.')
        val = val%20
    if val // 10 > 0:
        ced10 = val//10
        print(f'Receberá {ced10} cédulas de R$ 10,00.')
        val = val%10
    if val // 5 > 0:
        ced5 = val//5
        print(f'Receberá {ced5} cédulas de R$ 5,00.')
        val = val%5
    if val // 1 > 0:    
        ced1 = val//1
        print(f'E receberá {ced1} cédulas de R$ 1,00.')
    break

print('\n---FIM---\n')