
#Exemplo basico

lista1 = ['Um','Dois','Tres','Quatro']
lista2 = [1,2,3,4]
listaZip = zip(lista1,lista2)
print(listaZip)

#Exemplo Operacao

a = [1,3,5,6]
b = [2,6,7,9]

for i in zip(a,b):
	print(i[0]*i[1])
	
#Exemplo Dicionario

fruits = {
    'Laranjas': 7,
    'Abacaxis': 3,
    'Mangas': 5,
    'Goiabas': 5,
    'Cajus': 4,
}

lista = zip(fruits.keys(),fruits.values())
print(lista)

#Tamanhos diferentes de lista

a = [1,2,3,4,5]
b = [2,4,6,8,10,12]

c = zip(a,b)
print(c)


