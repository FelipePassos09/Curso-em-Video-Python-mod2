# Crie um programa que mostre uma contagem regressiva para o estouro de fogos de artifício
#, indo de 10 até 0, com uma pausa de 1s entre cada eles.


from time import sleep

for c in range(10, -1, -1):
    print('Faltam {}!!!!!'.format(c))
    sleep(1)
    print('')
    
print('FELIZ ANO NOVOOOOOOOO!!!!!\n')
    