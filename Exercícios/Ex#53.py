# Crie um programa que leia uma frase qualqeur e diga se ela é um Palíndromo, desconsiderando os espaços.


frase = str(input('Diga a frase que quer analisar.\n')).strip()
frasel = frase.replace(' ','').upper()

print('A frase {} ao contrário é {}.'.format(frasel, frasel[::-1]))
if frasel == frasel[::-1]:
    print('É palindromo')
else:
    print('Não é Palindromo.')
    
