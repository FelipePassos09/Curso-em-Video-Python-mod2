# Elabore um programa que calcule o valor a ser pago por um prduto considerando o seu preço normal e condição de pagamento:
 # A vista em dinheiro/cheque: 10% de desconto
 # A vista no cartão: 5% de desconto.
 # Em até 2X no cartão: preço normal.
 # 3x ou mais no cartão: 20% de juros.
 # Carnê: 25% de juros.
 
 ### Ao final diga qual o valor total do produto de acordo com a condição escolhida.

# Dicionário de cores
cores = {
    'azul' : '\033[34m',
    'verde' : '\033[32m',
    'amarelo' : '\033[33m',
    'negativo' : '\033[7;30m',
    'magenta' : '\033[35m',
    'vermelho' : '\033[1;31m',
    'limpa' : '\033[m'
}

# Váriáveis.
print('\033[33mCALCULADORA DE PREÇOS E PARCELAMENTO.\033[m')
preco = float(input('\nInforme o valor total do Item:\n'))
print(cores['magenta'])
parcelas = int(input('''
Informe em quantas parcelas pretende parcelar o produto através do menú abaixo:

1 - A Vista
2 - Em até 2x
3 - Em 3x ou mais

'''))
print(cores['azul'])
pag = int(input('''
Informe qual a forma de pagamento pretende utilizar:

1 - Dinheiro ou cheque.
2 - Cartão de crédito ou débito.
3 - Carnê ou financiamento.

'''))

d_cinco = preco * 0.05
d_dez = preco * 0.1
norm = preco
j_vinte = preco * 0.2
j_vintecinco = preco * 0.25
print(cores['limpa'])

# Estruturas e condições.
if parcelas == 1 and pag == 1:
    print('Ótimo, o cliente receberá um desconto de R$ {:.2f}.\n'.format(d_dez))
    print(cores['verde'],'O valor a pagar será R$ {}.\n'.format(preco - d_dez),cores['limpa'])
elif parcelas == 1 and pag == 2:
    print('Ótimo, o cliente receberá um desconto de R$ {:.2f}.\n'.format(d_dez))
    print(cores['verde'],'O valor a pagar será R$ {}.\n'.format(preco - d_dez),cores['limpa'])
elif parcelas == 2 and pag <= 2:
    print('Que pena, o cliente não receberá nenhum desconto.\n')
    print(cores['limpa'],'O valor a pagar será R$ {}.\n'.format(norm),cores['limpa'])
elif parcelas == 3 and pag == 2:
    print('Infelizmente teremos que aplicar R$ {:.2f} de juros.\n'.format(j_vinte))
    print(cores['vermelho'],'O valor a pagar será R$ {}.\n'.format(preco + j_vinte),cores['limpa'])
else:
    print('Infelizmente teremos que aplicar R$ {:.2f} de juros.\n'.format(j_vintecinco))
    print(cores['vermelho'],'O valor a pagar será R$ {}.\n'.format(preco + j_vintecinco),cores['limpa'])