import random

print('\033[33m-'*10,'\nJOGO DA ADIVINHAÇÃO!\n','-'*10,'\033[m')
computer = random.randrange(0,10,1)
user = int(input('\033[mAdivinhe o número que estou pensando: \n'))
control = 0

while user != computer:
  if user < computer:
    print ('Mais..')
  if user > computer:
    print('Menos..')
  user = int(input('\033[31mQue pena, ainda não, escolha novamente:\n\033[m'))
  control += 1

print('Você acertou em {} tentativas o número que escolhi foi {}.'.format(control+1, computer))