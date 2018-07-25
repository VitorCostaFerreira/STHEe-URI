# -*- coding: utf-8 -*-

numbers = list(map(float, input('').split()))
resultado = numbers[1]*numbers[2]
numbers1 = list(map(float, input('').split()))
resultado1 = numbers1[1]*numbers1[2]
total = resultado+resultado1
print('VALOR A PAGAR: R$ {:0.2f}'.format(total))