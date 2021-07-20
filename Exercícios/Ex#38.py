#  Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    # O primeiro valor é maior.
    # O segundo valor é maior.
    # Não existe valor maior, os dois são iguais.
    
print('\033[32m','-=-'*8,'\nVAMOS ANALISAR NÚMEROS!!!\n','-=-'*8,'\033[m')
nm1 = int(input('Diga um número inteiro qualquer: '))
nm2 = int(input('Agora diga outro número inteiro: '))

if nm1 == nm2:
    print('Ambos os números são iguais!')
    print('{} = {}'.format(nm1, nm2),'\033[m')
elif nm1 > nm2:
    print('\033[33mO primeiro número é maior que o segundo.')
    print('{} > {}'.format(nm1, nm2),'\033[m')
elif nm1 < nm2:
    print('\033[34mO segundo número é maior que o primeiro.')
    print('{} > {}2'.format(nm2, nm1),'\033[m')
    