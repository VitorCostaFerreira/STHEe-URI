import math
try:
    entrada = list(map(float, input('').split()))
    a = entrada[0]
    b = entrada[1]
    c = entrada[2]

    x=(b**2)-(4*a*c)
    x=math.sqrt(x)
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)

    print('R1 = {:0.5f}'.format(x1))
    print('R2 = {:0.5f}'.format(x2))
except:
    print('Impossivel calcular')