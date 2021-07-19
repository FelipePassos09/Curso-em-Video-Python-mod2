'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

A) qual é o total gasto na compra.
B) Quantos produtos custaram mais de R$ 1000.00.
C) Qual foi o produto mais barato comprado.

'''

print('\033[32m='*20)
print('\nLISTA DE COMPRAS\n')
print('='*20,'\033[m','\n')

cont = ['S','N']
total = quant = pricen = maiorq = 0
barato = ' '
caro = ' '

nome = str(input('Diga o seu nome:\n'))

while True:
    prod = str(input('Diga o nome do produto: \n'))
    price = float(input('Qual o preço do produto mencionado?\n'))

    quant += 1
    total += price
    
    if price > 1000:
        maiorq += 1
    
    if quant == 1:
        barato = caro = prod
        priceb = pricec = price
    elif price <= pricen and price <= priceb:
        barato = prod
        priceb = price
    elif price >= pricen and price >= pricec:
        caro = prod
        pricec = price
    
    pricen = price
    
    print(f'O total da sua compra até agora é R$ {total:.2f}.')
    print(f'Até o momento o mais barato é {barato.upper()} e o mais caro é {caro.upper()}.')
    
    cont = str(input('Quer continuar?\n[ S/N ]\n')).strip().upper()
    
    while cont not in ['S' , 'N']:
        cont = str(input('Quer continuar?\n[ S/N ]\n')).strip().upper()
        if cont in ['S' , 'N']:
            break        
    
    if cont == 'N':
        break

print(f'Sua compra deu um total de R$ {total:.2f}.')
print(f'Você comprou {maiorq} produtos custando mais de R$ 1000.00.')
print(f'Você comprou {quant} itens onde o mais caro foi {caro.upper()} e o mais barato {barato.upper()}.')
print(f'Obrigado pelas compras {nome.capitalize()}')
