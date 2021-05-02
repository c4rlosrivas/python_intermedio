#reduce
lista = [1, 4, 5, 6, 9, 13, 19, 21]
lista2 = list(filter(lambda x: x%2 != 0, lista))
print('resultado de filter: ',lista2)

#map
lista3 = [1, 2, 3, 4, 5]
lista4 = list(map(lambda x: x**2, lista))
print('resultado de map: ',lista4)

from functools import reduce
lista5 = [2, 2, 2, 2, 2]
lista6 = reduce(lambda a, b: a*b, lista5)
print('resultado de reduce: ',lista6)
