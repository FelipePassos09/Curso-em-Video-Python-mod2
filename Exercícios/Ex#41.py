#  A confederaçãod de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
     # Até 9 anos: MIRIM
     # Até 14 anos: INFANTIL
     # Até 19 anos: JUNIOR
     # Até 20 anos: SÊNIOR
     # Acima de 20 anos: MASTER
     
from datetime import datetime,date,time

dt_atual = str(date.today())
ano_n = int(input('Nos diga o ano em que nasceu: '))
ano_atual = date.today().year
idade = (ano_atual - ano_n)

print('Então você tem {} anos.'.format(idade))

if idade <= 9:
     print('Você é da categoria MIRIM.')
elif idade > 9 and idade <= 14:
     print('Você é da categoria INFANTIL.')
elif idade > 14 and idade <=19:
     print('Você é da categoria JUNIOR.')
elif idade > 19 and idade <= 20:
     print('Você é da categoria SÊNIOR.')
else:
     print('Você é da categoria MASTER.')