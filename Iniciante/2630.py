import math

X = int(input(''))

for i in range(1,X+1):
    OF = input('')
    
    Y = list(map(int,input('').split()))    
    
    if OF == 'mean':
        print('Caso #{}: {}'.format(i,math.floor((Y[0]+Y[1]+Y[2])/3)))
        
    elif OF == 'min':
        Y = sorted(Y)
        print('Caso #{}: {}'.format(i,Y[0]))
        
    elif OF == 'max':
        Y = sorted(Y)
        print('Caso #{}: {}'.format(i,Y[2]))

    elif OF == 'eye':
        print('Caso #{}: {}'.format(i,math.floor((Y[0]*0.30)+(Y[1]*0.59)+(Y[2]*0.11))))