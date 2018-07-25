try:    
    while True:
        X = list(map(int,input('').split()))
        A = X[0]
        B = X[1]
        C = X[2]
    
        if A == B == C:
            print('*')
        elif A != B == C:
            print('A')
        elif B != A == C:
            print('B')
        elif C != B == A:
            print('C')
except:
    quit()