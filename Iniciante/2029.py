try:
  N = 3.14
  while True:
    V = float(input(''))
    D = float(input(''))
    Altura = (V/(N*((D/2)**2)))
    Area = (N*((D/2)**2))
    print('ALTURA = {:0.2f}'.format(Altura))
    print('AREA = {:0.2f}'.format(Area))
except:
  quit()