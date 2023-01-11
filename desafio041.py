from datetime import date
print('--x----x--' * 5)
print('        Confederação Nacional de Natação'.upper())
print('--x----x--' * 5)
ano_nasc = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - ano_nasc
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <=14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade == 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
 