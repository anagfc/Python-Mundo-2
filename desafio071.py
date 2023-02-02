print('-' * 25)
print('{:^25}'.format('Banco Tech').upper())
print('-' * 25)
saque = int(input('Valor do saque: R$'))
valor = saque
cédula = 50
qtd_ced = 0
print('-' * 25)
print('{:^25}'.format('Seu saque'.upper()))
while True:
    if valor >= cédula:
        while valor >= cédula:
            valor -= cédula
            qtd_ced += 1
        print('{} cédulas de R${}'.format(qtd_ced, cédula)) 
    elif valor < cédula:
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 1
    qtd_ced = 0
    if valor == 0:
        print('-' * 25)
        break
