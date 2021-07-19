# Refaça o desafio 35 (dos triangulos) acrescentando o recurso de mostrar que tipo de triangulo será formado:
    # Equilatero se todos os lados forem iguais.
    # Isóceles se dois dos lados forem iguais.
    # Escaleno se todos os lados forem diferentes.
    
    
print('Vamos calcular um triangulo e ver de qual tipo ele será!!')

l1 = float(input('Diga o tamanho de uma reta: '))
l2 = float(input('Diga o tamanho de ourta reta: '))
l3 = float(input('Diga o tamanho da terceira reta: '))

print('-='*20)

if ((l3 + l1) > l2) and ((l2 + l3) > l1) and ((l1 + l2) > l3):
    print('Com essas retas conseguimos criar um triângulo.')
    # Condição aninhada:
    if l3 == l2 == l1:
        print('E ele será um triangulo EQUILATERO, já que todos os seus lados são iguais.')
    elif l3 != l2 and l3 != l1 and l1 != l2:
        print('E ele será um triangulo ESCALENO pois todos os seus lados são diferentes.')
    else:
        print('E ele será um triangulo ISÓCELES pois apenas dois de seus lados sã iguais.')
else:
    print ('Não conseguimos formar um triangulo com isso.')