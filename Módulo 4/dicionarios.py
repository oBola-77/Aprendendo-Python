#                                          Dicionários
# Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elemento em um dicionário consiste em uma chave única e seu valor correspondente. Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgulas.

#                                          Criação e acesso
# Para criar um dicionário, utilize chaves e separe as chaves e valores com dois pontos.
pessoa = {"nome": "Victor", "idade": 19, "cidade": "Poá"}

print("\nAcessando os valores do dicionario:")
print(pessoa["cidade"])
print(pessoa["nome"])
print(pessoa["idade"])
# Você também pode utilizar o método get() para obter o valor de uma chave. Se a chave não existir, retorna um valor padrão (por padrão, None).
print("\nUsando o metodo get():")
print("Estado:", pessoa.get("estado", "Não informado"))

#                                          Métodos de dicionários
# Os dicionários em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:
print("\nUsando metodos de dicionários:")
# keys(): retorna uma visualização de todas as chaves do dicionário.
print(pessoa.keys())

# values(): retorna uma visualização de todos os valores do dicionário.
print(pessoa.values())

# items(): retorna uma visualização de todos os pares chave-valor do dicionário.
print(pessoa.items())

# update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.
pessoa.update({"profissão": "Garoto de programa"})
print(pessoa)
