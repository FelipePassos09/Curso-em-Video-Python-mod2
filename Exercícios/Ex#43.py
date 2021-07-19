# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e moster seu status, de acordo com a tabela abaixo:
    # Abaixo de 18.5: Abaixo do peso.
    # Entre 18.5 e 25: Peso IDEAL
    # De 25 a 40: Obesidade
    # Acima de 40: Obesidade Mórbida
    
print('Calcule seu IMC!!!\n')
peso = float(input('Informe seu peso (no formato 0.00): \n'))
altura = float(input('Informe sua altura (no formato 0.00): \n'))

imc = peso/(altura**2)

if imc <= 18.5:
    print('\033[34mVocê está abaixo do peso, precisa de alimentar melhor.\nSeu IMC é {:.2f}'.format(imc), '\033[m')
elif imc > 18.5 and imc <= 25:
    print('\033[1;32mVocê está no peso ideal, parabéns.\nSeu IMC é {:.2f}'.format(imc),'\033[m')
elif imc > 25 and imc <= 40:
    print('\033[33mVocê está acima do peso, comece um regime.\nSeu IMC é {:.2f}'.format(imc),'\033[m')
else:
    print('\033[1;31mCUIDADO, você está com obesidade mórbida, procure ajuda o mais rápido possível.\nSeu IMC é {:.2f}'.format(imc),'\033[m')

