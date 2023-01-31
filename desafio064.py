número = 0
contador = 0
soma = 0
while número != 999:
    número = int(input('Insira um número: '))
    if número != 999:
        soma += número
        contador += 1
print('\nVocê inseriu {} números e a soma deles é {}.'.format(contador, soma))
