soma = 0
for c in range(0, 500):
    if (c[0] + c[1] + c[2]) % 3 == 0:
        soma =+ c
print('A soma dos números de 1 até 500 que são divisíveis por 3 é igual a {}.'.format(soma))