ini = c = int(input('Onde começa a PA: '))
fim = 10
salto = int(input('Qual será a razão da PA? '))

'''pa = range(ini, fim, salto)'''

cnt = 0

while cnt < fim:
    print(c, end=' ')
    c += salto
    cnt += 1
print('\nFIM!!')
print('Isso é tudo...')