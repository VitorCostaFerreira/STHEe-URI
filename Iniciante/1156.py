a = c = 0
b = 1
S = 0

for a in range(1,40,2):
    c=a/b
    S+=c
    b*=2

print('{:0.2f}'.format(S))