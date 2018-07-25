n = int(input(''))
final = list(range(n))
total = 0
for i in range(0,n):
    entrada = list(map(int,input('').split()))
    produto = entrada[0]
    preco = entrada[1]
    if produto == 1001:
        total += 1.50*entrada[1]
    elif produto == 1002:
        total += 2.50*entrada[1]
    elif produto == 1003:
        total += 3.50*entrada[1]
    elif produto == 1004:
        total += 4.50*entrada[1]
    elif produto == 1005:
        total += 5.50*entrada[1]

print('{:0.2f}'.format(total))