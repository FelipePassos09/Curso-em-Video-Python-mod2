# Faça um programa para aprovar um empréstimo bancário para comrpa de uma casa. Esse programa irá perguntar qual o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# calcule o valor da parcela sabendo que ele não pode exceder 30% do salário ou então o empréstio não será aprovado.


print('\033[33m','-\|/-'*8,'\nPrograma para avaliação de empréstimo.\n','-\|/-'*8,'\033[m','\n')
# Variaveis:

salario = float(input('Informe seu salário em R$: \n'))
valor_imv = float(input('Agora qual o valor do imóvel que deseja financiar: \n'))
tempo = int(input('Em quantos anos pretende pagar o imóvel? \n'))
parcela = (valor_imv / (tempo*12))
percentual_renda = (parcela / salario)*100

# Condições:
if parcela < (salario*0.30):
    print('\033[32m','\nTenho uma ótima notícia, o financeiamento foi aprovado.')
    print('A parcela será de R$ {:.2f}.'.format(parcela),'\033[m')
elif parcela == (salario*0.30):
    print('\nFoi por pouco, sua renda alcança o valor exato do limite para financiamento.')
    print('A parcela será de R$ {:.2f}.'.format(parcela))
else:
    print('\033[31m','\nDesculpe, seu financiamento não foi aprovado.')
    print('A parcela será de R$ {:.2f}, e isso representa {:.0f}% da sua renda.'.format(parcela,percentual_renda),'\033[m')
    
print('\n')

