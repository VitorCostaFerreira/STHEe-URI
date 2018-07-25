# -*- coding: utf-8 -*-

entrada = list(map(float, input('').split()))
area = (entrada[0]*entrada[2])/2
pi = 3.14159
areaR = pi*(entrada[2]**2)
areaT = ((entrada[0]+entrada[1])*entrada[2])/2
areaQ = (entrada[1]*entrada[1])
areaRec = (entrada[0]*entrada[1])
print('TRIANGULO: {:0.3f}'.format(area))
print('CIRCULO: {:0.3f}'.format(areaR))
print('TRAPEZIO: {:0.3f}'.format(areaT))
print('QUADRADO: {:0.3f}'.format(areaQ))
print('RETANGULO: {:0.3f}'.format(areaRec))