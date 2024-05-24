import random
from collections import Counter

lista = []

for i in range(1000):
    lista.append(random.randint(1,100))

c = Counter(lista)
nR = c.most_common(1)[0][0]
nU = min(c, key=c.get)

listaO = sorted(lista)
print(listaO)
print(nR)
print(nU)
print(lista)
#Mensaje