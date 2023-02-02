print('-' * 40)
print('{:^40}'.format('Cadastro de pessoas'.upper()))
print('-' * 40)
maiores = homens = mulheres = 0
while True:
    sexo = input('Insira o sexo [F/M]: ').strip().upper()
    while sexo != 'F' and sexo !='M':
        sexo = input('Insira o sexo [F/M]: ').strip().upper()
    if sexo == 'M':
        homens += 1
    idade = int(input('Insira a idade: '))
    if idade > 18:
        maiores += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    continuar = input('Cadastrar outra pessoa? [S/N]: ').strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Cadastrar outra pessoa? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    print('-' * 40)
print('\n{:^40}'.format('Analisando os dados'.upper()))
print('-' * 40)
print(f'{maiores} dos inseridos são maiores de idade.')
print(f'{mulheres} mulheres têm menos de 20 anos.')
print(f'{homens} homens inseridos no total.')
print('-' * 40)
    