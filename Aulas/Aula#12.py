name = str(input('Qual o seu nome: '))
nome = name.lower()
comuns = {'julia','beatriz','jessica','amanda','carol'}


if nome == 'felipe':
    print('Que nome bonito!!')
# Aqui podemos inserir um 'elif'.
elif nome == 'paulo' or nome == 'maria' or nome == 'joao':
    print('Seu nome é bem comum nesse país')
elif nome == 'marianna':
    print('Se for quem eu estou pensando vc deve ser linda!!!')
elif nome in comuns:
    print('Com esse nome vc deve ser mulher.')
# E podemos concluir com 'else'.
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome.capitalize()))
