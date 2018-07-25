try:
    X = int(input(''))
    total = cont = 0
    while True:
        Z = int(input(''))
    
        if X < Z:
            for i in range(X,Z+1):
                total += i
                cont += 1
                if total >= Z:
                    print(cont)
                    break
                else:
                    continue
        else:
            continue
except:
    quit()