nmr = int(input('Digite o número que quer extrair o fatorial:\n'))
controle = 1
ft=1

while nmr > 1:
  ft*=nmr
  nmr-=1
  controle +=1

print(f'O fatorial de {controle} é {ft}.')