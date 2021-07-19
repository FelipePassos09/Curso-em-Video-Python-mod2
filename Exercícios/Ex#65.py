cnt = 0
tot = 0
check = 'S'
maior = menor = 0

while check == 'S':
  nmr = int(input('Diga o numero que deseja somar: \n'))
  check = str(input('Deseja prosseguir? [S/N]\n')).upper()
  cnt += 1
  tot += nmr
  if cnt == 1:
    maior = menor = nmr
  else: 
    if nmr > maior:
      maior = nmr
    if nmr < menor:
      menor = nmr

média = tot / cnt

print('Você inseriu {} números.'.format(cnt))
print('O valor total foi {}.'.format(tot))
print('A média foi {}.'.format(média))
print('O maior numero foi {}.'.format(maior))
print('O menor numero foi {}.'.format(menor))