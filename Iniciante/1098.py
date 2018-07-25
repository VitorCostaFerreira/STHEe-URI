j = [0,0,0]
for i in range(0, 11):

    if i == 0:
        j[0] += 1
        j[1] += 2
        j[2] += 3
        print('I={} J={}'.format(i, j[0]))
        print('I={} J={}'.format(i, j[1]))
        print('I={} J={}'.format(i, j[2]))
    elif i == 1:
        print('I={:0.1f} J={}'.format(i-0.8, j[0]+0.2))
        print('I={:0.1f} J={}'.format(i-0.8, j[1]+0.2))
        print('I={:0.1f} J={}'.format(i-0.8, j[2]+0.2))
    elif i == 2:
        print('I={:0.1f} J={}'.format(i-1.6, j[0]+0.4))
        print('I={:0.1f} J={}'.format(i-1.6, j[1]+0.4))
        print('I={:0.1f} J={}'.format(i-1.6, j[2]+0.4))
    elif i == 3:
        print('I={:0.1f} J={}'.format(i - 2.4, j[0] + 0.6))
        print('I={:0.1f} J={}'.format(i - 2.4, j[1] + 0.6))
        print('I={:0.1f} J={}'.format(i - 2.4, j[2] + 0.6))
    elif i == 4:
        print('I={:0.1f} J={}'.format(i - 3.2, j[0] + 0.8))
        print('I={:0.1f} J={}'.format(i - 3.2, j[1] + 0.8))
        print('I={:0.1f} J={}'.format(i - 3.2, j[2] + 0.8))
    elif i == 5:
        print('I={} J={}'.format(i - 4, j[0] + 1))
        print('I={} J={}'.format(i - 4, j[1] + 1))
        print('I={} J={}'.format(i - 4, j[2] + 1))
    elif i == 6:
        print('I={:0.1f} J={}'.format(i-4.8, j[0]+1.2))
        print('I={:0.1f} J={}'.format(i-4.8, j[1]+1.2))
        print('I={:0.1f} J={}'.format(i-4.8, j[2]+1.2))
    elif i == 7:
        print('I={:0.1f} J={}'.format(i - 5.6, j[0] + 1.4))
        print('I={:0.1f} J={}'.format(i - 5.6, j[1] + 1.4))
        print('I={:0.1f} J={}'.format(i - 5.6, j[2] + 1.4))
    elif i == 8:
        print('I={:0.1f} J={}'.format(i-6.4, j[0]+1.6))
        print('I={:0.1f} J={}'.format(i-6.4, j[1]+1.6))
        print('I={:0.1f} J={}'.format(i-6.4, j[2]+1.6))
    elif i == 9:
        print('I={:0.1f} J={}'.format(i-7.2, j[0]+1.8))
        print('I={:0.1f} J={}'.format(i-7.2, j[1]+1.8))
        print('I={:0.1f} J={}'.format(i-7.2, j[2]+1.8))
    elif i == 10:
        print('I={} J={}'.format(i - 8, j[0] + 2))
        print('I={} J={}'.format(i - 8, j[1] + 2))
        print('I={} J={}'.format(i - 8, j[2] + 2))
        break