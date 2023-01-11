nome = input('Insira seu nome: ').title()
print('Olá, {}.'.format(nome))
n1 = float(input('Insira a 1ª nota: '))
n2 = float(input('Insira a 2ª nota: '))
média = (n1 + n2) / 2

if média < 5:
    print('{}, você foi REPROVADO.'.format(nome))
    
elif média > 5 and média < 6.9:
    print('{}, você está em RECUPERAÇÃO.'.format(nome))
else:
    print('{}, você foi APROVADO.'.format(nome))