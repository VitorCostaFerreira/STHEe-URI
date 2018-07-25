j = 65

for i in range(1, j, 3):
    if i+3:
        j -= 5
        print('I={} J={}'.format(i,j))
        if j == 0:
            final = i
            quit()
    else:
        estouro = i