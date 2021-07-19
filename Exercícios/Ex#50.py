# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for impar, desconsidere-o.

cont = 0
nm = 0
for i in range(0, 6, 1):
    i = int(input('Diga um número qualquer:'))
    cont +=1
    if i % 2 == 0:
        nm += i
print('Entre os {} números informados, a soma dos números pares foi {}.'.format(cont, nm))

        
