número = int(input('Fatorial desejado: '))
fatorial = 1
for c in range (número, 1, -1):
    fatorial *= c
    c += 1
print('{}! é igual a {}.'.format(número, fatorial))
