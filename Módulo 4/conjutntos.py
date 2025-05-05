#                                        Conjuntos (set)
# Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().

#                                        Criação e operações básicas
# Para criar um conjunto, utilize chaves ou a função set():
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

# Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
print("\nMostrando os conjutnos:")
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4 ,5}
print(conjunto1)
print(conjunto2)

print("\nUsnado o operador de Uniao(|):")
uniao = conjunto1 | conjunto2
print(uniao)

print("\nUsnado o operador de Interseção(&):")
intersecao = conjunto1 & conjunto2
print(intersecao)

print("\nUsnado o operador de Diferença(-):")
diferenca = conjunto1 - conjunto2
print(diferenca)

print("\nUsnado o operador de Diferença_simetirca(^):")
diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)

#                                           Métodos de conjuntos
# Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

# add(elemento): adiciona um elemento ao conjunto.
print("\nAdicionando uma fruta nova no conjutno:")
frutas.add("pitaya")
print(frutas)

# remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
print("\nRemovendo uma fruta do meu conjunto")
frutas.remove("laranja")
print(frutas)

# discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
print("\nTirando um elemento que n existe no conjunto (n acontece nada =) )")
frutas.discard("uva")
print(frutas)

# clear(): remove todos os elementos do conjunto.
print("\nLimpando todos os elemntos dentro do meu conjutno")
frutas.clear()
print(frutas)
