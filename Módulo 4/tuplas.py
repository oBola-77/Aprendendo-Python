#                                       Criação e acesso
# Para criar uma tupla, encerre os elementos entre parênteses:
ponto = (6, 9)
print(ponto[0]) # Pegando o elemento em uma posição especifica
print(ponto[1]) # Pegando o elemento em uma posição especifica

#                                       Métodos de tuplas
# Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas:

# count(elemento): devolve o número de vezes que um elemento aparece na tupla.
minha_tupla = (1, 2, 3, 2, 4, 2)
print(minha_tupla.count(2))

# index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
print(minha_tupla.index(2, 2))

# len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.
tamanho = len(minha_tupla)
print(tamanho)