# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    ## 1 para binário
    ## 2 para octal
    ## 3 para hexadecimal
    
    
import math
    
print('\033[32m','##'*25,'\nEsse é o nosso conversor universal para números binários, octais e hexadecimais\n', '##'*25,'\033[m')
núm = int(input('Qual o número que deseja converter: \n'))
opção = int(input('''
Qual conversão deseja fazer?
                  
1 : Binário
2 : Octal
3 : Hexadecimal

Digite a opção:
'''))

print('\033[2;33m')

if opção == 1:
    print('O número {} convertido para BINÁRIO é {}.'.format(núm, bin(núm)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é {}.'.format(núm, oct(núm)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é {}.'.format(núm, hex(núm)[2:]))
else:
    print('\033[2;31mOpção inválida!!')
    
print('\033[m')