op = 0
nm1 = int(input('Diga o primeiro valor:\n'))
nm2 = int(input('Diga o segundo valor.\n'))
while op != 5:
  op = int(input('''
Diga qual operação quer realizar:
[1] Soma
[2] Multiplicação
[3] Comparação
[4] Entrar novos números
[5] Encerrar Programa
  '''))
  if op == 1:
    print('A soma de {} e {} é {}.'.format(nm1, nm2, nm1 + nm2))
  elif op == 2:
    print('A multiplicação de {} e {} é {}.'.format(nm1, nm2, nm1 * nm2))
  elif op == 3:
    if nm1 > nm2:
      print('O primeiro valor({}) é maior que o segundo valor({}).'.format(nm1, nm2))
    elif nm2 >nm1:
      print('O segundo valor ({}) é maior que o primeiro valor ({}).'.format(nm2, nm1))
    else:
      print('Os dois valores são iguais.')
  elif op == 4:
    nm1 = int(input('Diga o primeiro valor:\n'))
    nm2 = int(input('Diga o segundo valor.\n'))

print('OK, programa encerrado.')