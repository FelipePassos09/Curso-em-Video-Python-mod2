# Crie um programa que mostre todos os números pares entre 1 e 50.

print('Os números pares são: ',end = ' ')

for n in range(2, 51, 2):
    print('{}'.format(n), end=' ')
    
print('\nAcabou!')
