início = int(input('Primeiro termo da P.A.: '))
razão = int(input('Razão da P.A.: '))

for c in range(1, 11):
    ac = início + (c-1) * razão
    print(ac, end='... ')
    