while True:
    P = int(input())

    if P < 0:
        break
    else:
        if P-1 < 0:
            print('0')
        else:
            print(P-1)

'''
0
1
10000000000000000000
-1
'''