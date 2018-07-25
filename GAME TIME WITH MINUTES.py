entrada = list(map(int, input('').split()))

A = entrada[0] #HORAS
B = entrada[1] #MINUTES
C = entrada[2] #HORAS
D = entrada[3] #MINUTES

teste = (A*60)+B
teste1 = (C*60)+D

#print(teste)
#print(teste1)

if teste1 > teste:
  total = teste1-teste
  
  minutos = ((total%60)-total)+total
  if minutos >= 59:
    hora = 0
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora,minutos))
  else:
    hora = total%60
    print('O JOGO DUROU {} HORA(S)'.format(hora),end=' ')
    print('E {} MINUTO(S)'.format(minutos))

if teste > teste1:
  total = teste-teste1

  minutos = ((total%60)-total)+total
  if minutos >= 59:
    hora = 0
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora,minutos))
  else:
    hora = total%60
    print('O JOGO DUROU {} HORA(S)'.format(hora),end=' ')
    print('E {} MINUTO(S)'.format(minutos))

if teste == teste1:
  print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')