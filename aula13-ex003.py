n = int(input('Insira um número: '))
for c in range (0, n+1):
    print(c)
print('Fim!')

print('\n')

i = int(input('Início da contagem: '))
f = int(input('Final da contagem: '))
p = int(input('Passo da contagem: '))

for c in range (i, f+1, p):
    print(c)
print('Fim!')