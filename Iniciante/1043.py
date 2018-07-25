entrada = list(map(float, input('').split()))

if (entrada[0]) >= (entrada[1]+entrada[2])or(entrada[1]) >= (entrada[2]+entrada[0])or (entrada[0] + entrada[1]) <= (entrada[2]):
    AreaTrapezio = ((entrada[0]+entrada[1])*entrada[2])/2
    print('Area = {:0.1f}'.format(AreaTrapezio))
else:
    Perimetro = entrada[0]+entrada[1]+entrada[2]
    print('Perimetro = {}'.format(Perimetro))