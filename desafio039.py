import datetime

nome = input('Nome completo: ')
dia = int(input('Dia do nascimento: '))
mês = int(input('Mês do nascimento: '))
ano = int(input('Ano do nascimento: '))
nascimento = datetime.date(ano, mês, dia)
idade_anos = date.today().year - ano

print('-=-' * 15)
if idade_anos < 18:
    print('{}, você deverá se alistar em {} dias, {} meses e {} anos.'.format())    
elif idade_anos == 18:
    print('{}, você deve se alistar agora.')
else:
    print('{}, você se alistou há {} dias, {} meses e {} anos.'.format())
print('-=-' * 15)
