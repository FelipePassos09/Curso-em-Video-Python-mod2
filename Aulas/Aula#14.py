valor = 's'
while valor in ('s','S'):
  data_nasc = input('Informe a data de nascimento do usuário:\n').strip().lower()
  valor = input('''
  Quer continuar jogando?
  [S] - SIM
  [N] - NÃO
  ''').strip().lower()
  
  