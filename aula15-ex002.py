print('Exemplo 01')
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    
#999 é a flag, o que sinaliza a parada

print('\nExemplo 02')
n = s = 0
while True: #Faria looping infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.')
