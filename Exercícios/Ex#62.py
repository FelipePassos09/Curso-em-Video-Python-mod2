ini = c = int(input('Onde começa a PA: '))
salto = int(input('Qual será a razão da PA? '))
total = 0
mais = 10
'''pa = range(ini, fim, salto)'''

cnt = 0

while mais != 0:
  total += mais
  while cnt <= total:
    print(c, end=' ')
    c += salto
    cnt += 1
  mais = int(input('\nQuer mostrar mais quantos items?\n'))
print('\nFIM!!')
print('Isso é tudo...')
