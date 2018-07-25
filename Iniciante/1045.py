entrada = list(map(float, input('').split()))

a = entrada[0]
b = entrada[1]
c = entrada[2]
test = sorted([a,b,c])

org = test[::-1]

A = org[0]
B = org[1]
C = org[2]

if A >= B+C:
    print('NAO FORMA TRIANGULO')
    quit()
if A**2 == B**2+C**2:
    print('TRIANGULO RETANGULO')
if A**2 > B**2+C**2:
    print('TRIANGULO OBTUSANGULO')
if A**2 < B**2+C**2:
    print('TRIANGULO ACUTANGULO')
if A == B == C:
    print('TRIANGULO EQUILATERO')
if (A == B and A != C)or(B == C and B != A)or(C == A and C != B):
    print('TRIANGULO ISOSCELES')