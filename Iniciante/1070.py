n = int(input(''))
cont = 99999999
stop = 0
for i in range(n,cont+12):
    if i%2 == 0:
        i = i
    else:
        print(i)
        stop += 1
        if stop == 6:
            quit()
