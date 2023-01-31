inserir = 'S'
soma = 0
contador = 0
maior = 0
menor = 0
while inserir == 'S':
    número = int(input('Insira um número: '))
    if maior == 0 and menor == 0:
        maior = número
        menor = número
    if número > maior:
        maior = número
    if número < menor:
        menor = número
    contador += 1
    soma += número
    inserir = input('Deseja inserir mais números? [S/N]: ').upper().strip()
média = soma / contador
print('\nVocê inseriu {} números. A média deles é {:.1f}.'.format(contador, média))
print('O maior número inserido foi {} e o menor foi {}.'.format(maior, menor))
