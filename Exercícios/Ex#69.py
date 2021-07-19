'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar, no final mostre:

[A] quantas pessoas tem mais de 19 anos.
[B] quantos homens foram cadastrados.
[C] quantas mulheres, com menos de 20 anos, foram cadastradas.
'''

from datetime import date

atual = date.today().year

idade = ' '
sexo = ' '
conth = contm = contm20 = 0
continua = 'S'

while True:     
    idade = int(input('Informe o ano de nascimento do usuário: \n'))
    sexo = str(input('Informe o sexo do usuário [ M/F ]: \n')).strip().upper()
    while sexo not in ['M' , 'F']:
        sexo = str(input('ERRADO!\nInforme o sexo do usuário [ M/F ]: \n')).strip().upper()
        if sexo in ['M' , 'F']:
            break
    continua = str(input('Quer continuar?\n[ S/ N ]\n')).strip().upper()
    while continua not in ['S' , 'N']:
        continua = str(input('ERRADO!\nInforme a opção correta [ S/N ]: \n')).strip().upper()
        if continua in ['S' , 'N']:
            break
        
    if sexo == 'M':
        conth += 1
    if sexo == 'F':
        contm += 1
        if (atual - idade) < 20:
            contm20 += 1
    if continua == 'N':
        break

print(f'Foram informados {conth} homens e {contm} mulheres, sendo que {contm20} tem menos de 20 anos.')