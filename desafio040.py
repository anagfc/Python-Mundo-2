nome = input('Insira seu nome: ').title()
print('Olá, {}.'.format(nome))
n1 = float(input('Insira a 1ª nota: '))
n2 = float(input('Insira a 2ª nota: '))
média = (n1 + n2) / 2

if média < 5:
    print('\n{}, sua média foi {:.1f}.'.format(nome, média))
    print('Status: REPROVADO.')
    
elif média >= 5 and média < 6.9: #Pode ser usado: 6.9 > média >= 5
    print('\n{}, sua média foi {:.1f}.'.format(nome, média))
    print('Status: RECUPERAÇÃO.')
else:
    print('\n{}, sua média foi {:.1f}.'.format(nome, média))
    print('Status: APROVADO.')
    