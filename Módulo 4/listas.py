#                                                       Listas

#   Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma lista podem ser de diferentes tipos de dados e são encerrados entre colchetes [], separados por vírgulas.

frutas = ["Banana", "Maçã", "Uva"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

#   Você também pode acessar os elementos a partir do final da lista utilizando índices negativos. O índice -1 representa o último elemento, -2 representa o penúltimo, e assim por diante.
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

#                                               Métodos de listas

# As listas em Python têm vários métodos incorporados que nos permitem manipular e modificar os elementos da lista. Alguns métodos comuns são:

# append(elemento): adiciona um elemento ao final da lista.
frutas.append("Pera")
print(frutas)

# insert(indice, elemento): insere um elemento em uma posição específica da lista.
frutas.insert(1, "Laranja")
print(frutas)

# remove(elemento): remove a primeira ocorrência de um elemento na lista.
frutas.remove("Banana")
print(frutas)

# pop(indice): remove e retorna o elemento em uma posição específica da lista.
frutaRemovida = frutas.pop(3)
print(frutaRemovida)

# sort(): ordena os elementos da lista em ordem ascendente.
frutas.sort()
print(frutas)

# reverse(): inverte a ordem dos elementos na lista.
frutas.reverse()
print(frutas)

#                                               Listas de compreensão

# As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.
numeros = [1, 2, 3, 4, 5, 6]
quadros = [x ** 2 for x in numeros if x % 2 == 0]
print(quadros)
# Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números. A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.

