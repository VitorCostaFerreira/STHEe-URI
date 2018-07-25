# -*- coding: utf-8 -*-

from math import sqrt
l1 = list(map(float, input('').split()))
l2 = list(map(float, input('').split()))
Distance = sqrt(((l2[0]-l1[0])**2)+((l2[1]-l1[1])**2))
print('{:0.4f}'.format(Distance))