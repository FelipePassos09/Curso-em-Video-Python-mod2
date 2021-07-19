nmr = 0
total = 0
cnt = 0

while nmr != 999:
  nmr =int(input('Diga o numero que deseja somar: '))  
  if nmr != 999:    
    total += nmr
    cnt = cnt + 1

print('Você digitou {} números e a soma entre eles é {}.'.format(cnt, total))