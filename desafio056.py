soma_idade = 0
homem_velho = 0
mulher_menos = 0

for c in range(0, 4):
    print('\n- - - - {}ª pessoa - - - -'.format(c+1).upper())
    nome = input('Insira seu nome: ').title()
    idade = int(input('Insira sua idade: '))
    sexo = input('Insira seu sexo (F/M): ').upper()
    
    soma_idade = soma_idade + idade
    
    if sexo == 'M' and idade > homem_velho:
        nome_homem_velho = nome
        homem_velho = idade
    if sexo == 'F' and idade < 20:
        mulher_menos = mulher_menos +1

print('\n')
print('A média das idades inseridas é de {:.1f} anos.'.format(soma_idade/4))
print('O homem mais velho é {}, com {} anos.'.format(nome_homem_velho, homem_velho))
print('{} das mulheres inseridas tem menos de 20 anos.'.format(mulher_menos))
