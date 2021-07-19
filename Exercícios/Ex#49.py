# Refaça o desafio 9 mostrando uma tabuada de um número que o usuário escolher, só que usando for.

# Input do valor a ser calculado:
multi = int(input('Insira o número que deseja multiplicar: '))

# Inicio dos parâmetros de range:
inicio = int(input("Diga de onde quer começar a calcular: "))
fim = int(input("Diga quando quer parar de calcular: "))
passo = 1


# Algoritmo de cálculo:
multiplos = list(range(inicio, fim + 1, passo))

print('Usando listas:\n\nA tabuada de {} é:'.format(multi))
for item in multiplos:
    result = (item * multi)
    print('{} vezes {} é {}'.format(item, multi, result))

print('Isso é tudo por enquanto.\n----------------')