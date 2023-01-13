from datetime import date, timedelta
nome = input('Nome completo: ').title()
nomef = nome.split()
sexo = input('Insira o sexo (F/M): ').upper()
if sexo == "F":
    print('{}, Você não precisa se alistar.'.format(nomef[0]))
else:
    dia_nascimento = int(input('Insira o dia do seu nascimento: '))
    mês_nascimento = int(input('Insira o mês do seu nascimento: '))
    ano_nascimento = int(input('Insira o ano do seu nascimento: '))
    idade = date.today().year - ano_nascimento
    nascimento = date(ano_nascimento, mês_nascimento, dia_nascimento)
    data_atual = date.today()
    ano_atual = date.today().year
    mês_atual = date.today().month
    dia_atual = date.today().day
    if idade == 18 and mês_nascimento == mês_atual: #idade 18 mês do aniversário
        if dia_nascimento > dia_atual: #18 anos incompletos por dias
            print('Status de {}'.format(nome))
            print('Ainda faltam {} dias para você se alistar.'.format((dia_nascimento - dia_atual)))
        elif dia_nascimento == dia_atual: #dia do aniversário
            print('Status de {}'.format(nome))
            print('Você deve se alistar agora.')
        else: # 18 anos completos
            print('Status de {}'.format(nome))
            print('Você se alistou há {} dias.'.format((dia_atual - dia_nascimento)))
    elif idade == 18 and mês_nascimento > mês_atual: #18 anos incompletos por meses
        d1 = date(ano_atual, mês_nascimento, dia_nascimento)
        tdelta = (d1 - data_atual) #Quantos dias faltam até o aniversário
        print('Status de {}:'.format(nome))
        print('Você deverá se alistar em {}.'.format(tdelta))
    elif idade == 18 and mês_nascimento < mês_atual: #18 anos completos no ano
        d1 = date(ano_atual, mês_nascimento, dia_nascimento)
        tdelta = (data_atual - d1)
        print('Status de {}'.format(nome))
        print('Você se alistou há {}.'.format(tdelta))
    elif idade < 18:
        anos = 18 - idade
        print('Status de {}'.format(nome))
        print('Você deverá se alistar em {} anos.'.format(anos))
    else:
        anos_de_alistamento = ano_atual - ano_nascimento - 18
        print('Status de {}'.format(nome))
        print('Você se alistou há {} anos.'.format(anos_de_alistamento))
    