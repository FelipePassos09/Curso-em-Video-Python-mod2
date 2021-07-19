# Crie unm programa que leia duas notas de um aluno e calcule sua média, mostrando uam mensagem no final de acordo com a média atingida:
    # Média abaixo de 5.0: REPROVADO
    # Média entre 5.0 e 6.9: RECUPERAÇÃO
    # Média 7.0 ou maior: APROVADO
    
print('Calculadora Escolar')
print('')
print('''
Aqui temos uma calculadora de médias, para saber se você passou na matéria.
      
Considerando que a nota máxima de cada exame é 10.0.
      ''')
nt1 = float(input('Diga qual a nota da sua prova: '))
nt2 = float(input('Diga qual a nota do trbalho: '))
print('')
media = ((nt1 + nt2) / 2)

if media <= 5:
    print('\033[31mVocê foi reprovado, terá de repetir a matéria.')
elif media > 5 and media < 7:
    print('\033[33mVocê não foi reprovado, mas pegou recuperação.')
elif media >= 7:
    print('\033[32mParabéns, você passou na matéria.')
    
print('\033[m')

print('É isso, quando precisar estarei por aqui.')
    
