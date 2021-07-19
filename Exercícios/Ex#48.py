# Faça um prgrama que calcule a soma entre todos os números impares que são multiplos de três e 
# que se encontram no intervalo entre 1 e 500:

cont = 0
soma = 0
for n in range(1, 500, 1):
    if n % 3 == 0 and n % 2 != 0:
        soma += n
        cont +=1
print('A soma de todos os {} valores entre 1 e 500 é: {}'.format(cont , soma))