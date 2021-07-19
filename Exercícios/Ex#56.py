# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre:
    # A média de idade do grupo.
    # Qual o nome do homem mais velho.
    # Quantas mulheres tem menos de 20 anos.
    
from datetime import date

# Variáveis de controle:
idadeh = 0
nm_h = ''
nm_m = ''
sx = ''
idadem = 0
somaidade = 0

# Objetos principais:
ano_at = date.today().year

# Algoritmo:

for i in range(1, 5, 1):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Diga o nome da {}ª pessoa:\n'.format(i))).upper().strip()
    sexo = str(input('Qual o sexo da {}ª pessoa (m/h):\n'.format(i))).upper().strip()
    idadei = int(input('Por fim, em que ano nasceu a pessoa?\n'))
    somaidade += (ano_at - idadei)
    if i == 1:
        if sexo == 'H':
            nm_h = nome
            idadeh = ano_at - idadei
        else:
            nm_m = nome
            idadem += 1
    else:
        if sexo == 'H' and (ano_at - idadei) > idadeh:
            nm_h = nome
            idadeh = ano_at - idadei
        if sexo == 'M':
            if (ano_at - idadei) < 20:
                idadem += 1
                
média_idade = somaidade/i            
        
print('O homem mais velho é {}, com {} anos.'.format(nm_h,idadeh))
print('A média_idade do grupo é {} anos.'.format(média_idade))
print('Existem {} mulheres com menos de 20 anos.'.format(idadem))

            
