T = int(input(''))
total = 0
N = list(map(int,input('').split()))
for i in range(0,len(N)):
  if T in N:
    N.remove(T)
    total += 1
print(total)