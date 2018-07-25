N = int(input(''))
alunoFinal = notaFinal = 0
for i in range(0,N):
    entrada = list(map(float,input('').split()))
    aluno = entrada[0]
    nota = entrada[1]
    if nota >= 8 and notaFinal < nota:
        alunoFinal = aluno
        notaFinal = nota
    else:
        continue

if alunoFinal == 0:
    print('Minimum note not reached')
else:
    print(int(alunoFinal))