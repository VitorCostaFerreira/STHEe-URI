entrada = list(map(int, input('').split()))

CachorroQuente = [1,'Cachorro Quente',4.00]
XSalada = [2,'X-Salada',4.50]
XBacon = [3,'X-Bacon',5.00]
TorradaSimples = [4,'Torrada simples',2.00]
Refrigerante = [5,'Refrigerante',1.50]

condiçoes = [CachorroQuente[0],XSalada[0],XBacon[0],TorradaSimples[0],Refrigerante[0]]
preços = [CachorroQuente[2],XSalada[2],XBacon[2],TorradaSimples[2],Refrigerante[2]]

if entrada[0] == 1:
    total1 = entrada[1]*preços[0]
    print('Total: R$ {:0.2f}'.format(total1))
if entrada[0] == 2:
    total2 = entrada[1]*preços[1]
    print('Total: R$ {:0.2f}'.format(total2))
if entrada[0] == 3:
    total3 = entrada[1]*preços[2]
    print('Total: R$ {:0.2f}'.format(total3))
if entrada[0] == 4:
    total4 = entrada[1]*preços[3]
    print('Total: R$ {:0.2f}'.format(total4))
if entrada[0] == 5:
    total5 = entrada[1]*preços[4]
    print('Total: R$ {:0.2f}'.format(total5))