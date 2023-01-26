jovens = 0
velhos = 0
from datetime import date
for c in range(0, 7):
    ano_nascimento = int(input('Insira o {}º ano de nascimento: '.format(c+1)))
    idade = date.today().year - ano_nascimento
    if idade > 21:
        velhos += 1
    else:
        jovens += 1
print('\nNos dados inseridos, temos:\n{} maiores de idade\n{} menores de idade'.format(velhos, jovens))
