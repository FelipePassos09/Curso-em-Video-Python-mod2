nmr = int(input('Informe um número:'))

n1,n2 = 0, 1
cnt = 0
fb = 1
print('Essa é a Sequência Fibonacci:')
while cnt < nmr:
	print(n1, end = '→')
	fb = n1 + n2
	n1 = n2
	n2 = fb
	cnt += 1
  