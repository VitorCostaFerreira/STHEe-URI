def fibonacci(n):
    f = [0]
    a, b = 0, 1
    while True:
        if len(f) == n:
            break
        f.append(b)
        a, b = b, a+b
    return f

x = int(input()) 
print(" ".join([str(x) for x in fibonacci(x)]))