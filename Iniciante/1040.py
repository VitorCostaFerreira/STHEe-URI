entrada = list(map(float, input('').split()))


peso1 = 2
peso2 = 3
peso3 = 4
peso4 = 1

n1 = entrada[0]*peso1
n2 = entrada[1]*peso2
n3 = entrada[2]*peso3
n4 = entrada[3]*peso4

media = (n1+n2+n3+n4)/(peso1+peso2+peso3+peso4)

if media >= 7.0:
    print('Media: {:0.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5.0:
    print('Media: {:0.1f}'.format(media))
    print('Aluno reprovado.')
elif 5.0 <= media <= 6.9:
    exame = float(input(''))
    print('Media: {:0.1f}'.format(media))
    print('Aluno em exame.')
    print('Nota do exame: {:0.1f}'.format(exame))
    total = (media+exame)/2
    if total >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:0.1f}'.format(total))
    elif total <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {:0.1f}'.format(total))

