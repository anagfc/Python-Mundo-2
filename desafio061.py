print('-' * 20)
print('{:^20}'.format('Criador de PA'))
print('-' * 20)
início = int(input('1º termo da PA: '))
razão = int(input('Razão da PA: '))
exibir = 1
while exibir < 11:
    termo = início + (exibir - 1) * razão
    print(termo, end='... ')
    exibir += 1
