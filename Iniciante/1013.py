# -*- coding: utf-8 -*-
for i in range(0,1):
    ent = list(map(int, input('').split()))
    if i == 0:
        maior = ent[0]
        if ent[1] > maior:
            maior = ent[1]
        if ent[2] > maior:
            maior = ent[2]
print('{} eh o maior'.format(maior))