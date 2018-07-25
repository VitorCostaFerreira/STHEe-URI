a,b,c = map(int,input().split())

if (a>b):
    if (b>c):
        if ((b-c)<(a-b)):
            print(':)')
        else:
            print(':(')
    else:
        print(':)')
elif(b>a):
    if(c>b):
        if ((c-b)<(b-a)):
            print(':(')
        else:
            print(':)')
    else:
        print(':(')
elif(c>b):
    print(':)')
else:
    print(':(')