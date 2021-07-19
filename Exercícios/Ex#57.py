sexo = ('M','F')
sx = ''
c = str(input('Diga o sexo do usuário:\n'))



while c not in sexo:
  c = str(input('Errado.\nDiga o sexo do usuário [M] ou [F]:\n')).strip().upper()
  if c in sexo:

    if c == 'M':
      sx = 'MASCULINO'
    if c == 'F':
      sx = 'FEMININO'

    print('O sexo do usuário é {}.'.format(sx))

  else:
    print('Errado, tente novamente.\n')