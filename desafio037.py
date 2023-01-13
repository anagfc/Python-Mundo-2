n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binária
[2] Octal
[3] Hexadecimal''')
escolha = int(input('Conversão para: '))
if escolha == 1:
    print('{} convertido para binário: {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para octal: {}'.format(n, oct(n)[2:]))
elif escolha ==3:
    print('{} convertido para hexadecimal: {}'.format(n, hex(n)[2:]))
else:
    print('Escolha inválida.')