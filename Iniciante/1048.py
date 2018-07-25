salario = float(input(''))

if salario <= 400.00:
    adicional = salario*(15/100)
    reajustado = salario+adicional
    percentual = '15 %'
    print('Novo salario: {:0.2f}'.format(reajustado))
    print('Reajuste ganho: {:0.2f}'.format(adicional))
    print('Em percentual: {}'.format(percentual))
elif 400.01 <= salario <= 800.00:
    adicional = salario*0.12
    reajustado = salario+adicional
    percentual = '12 %'
    print('Novo salario: {:0.2f}'.format(reajustado))
    print('Reajuste ganho: {:0.2f}'.format(adicional))
    print('Em percentual: {}'.format(percentual))
elif 800.01 <= salario <= 1200.00:
    adicional = salario*0.10
    reajustado = salario+adicional
    percentual = '10 %'
    print('Novo salario: {:0.2f}'.format(reajustado))
    print('Reajuste ganho: {:0.2f}'.format(adicional))
    print('Em percentual: {}'.format(percentual))
elif 1200.01 <= salario <= 2000.00:
    adicional = salario*0.07
    reajustado = salario+adicional
    percentual = '7 %'
    print('Novo salario: {:0.2f}'.format(reajustado))
    print('Reajuste ganho: {:0.2f}'.format(adicional))
    print('Em percentual: {}'.format(percentual))
elif salario >= 2000.01:
    adicional = salario*0.04
    reajustado = salario+adicional
    percentual = '4 %'
    print('Novo salario: {:0.2f}'.format(reajustado))
    print('Reajuste ganho: {:0.2f}'.format(adicional))
    print('Em percentual: {}'.format(percentual))