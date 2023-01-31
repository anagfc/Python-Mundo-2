print('-' * 20)
print('{:^20}'.format('Criador de PA'))
print('-' * 20)
início = int(input('1º termo da PA: '))
razão = int(input('Razão da PA: '))
termo = início
termos = 1
total_termos = 0
mais = 10
while mais != 0:
    total_termos += mais
    while termos <= total_termos:
        print(termo, end = '... ')
        termo += razão
        termos += 1
    print('Pausa')
    mais = int(input('Quantos termos deseja ver a mais? '))
print('\nVocê visualizou {} termos da PA.'.format(total_termos))
