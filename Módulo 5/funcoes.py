# #                                             Definição e chamada de funções
# # Para definir uma função em Python, utilizamos a palavra-chave def seguida do nome da função e parênteses. Opcionalmente, podemos especificar parâmetros dentro dos parênteses. O bloco de código da função é indentado após os dois pontos.

def saudacao():
     print("Olá mundo!")
saudacao()

# #                                              Parâmetros e argumentos
# # As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os parâmetros são especificados dentro dos parênteses na definição da função.

def saudação(nome):
     print(f"Olá, {nome}!")
saudação("Victor")

# #                                               Valores de retorno
# # As funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função.

def soma(a, b):
    return a + b
resultado = soma(3, 4)
print(resultado)

# #                                               Funções anônimas (lambda)
# # Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

quadrado = lambda x: x**2
print(quadrado(5))

#                                               Escopo das variáveis (local vs. global)
# As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.

def funcao():
    variavel_local = 300
    print(variavel_local)

variavel_global = 45

def funcao2():
    print(variavel_global)

funcao()
funcao2()

#                                               Funçoes definidas por usuário

def calcularMedia(*notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    return media
    
print(f"A sua média foi de: {calcularMedia(8, 9, 4, 5, 10, 7):.2f}")


somar = lambda x: x + 4342
print("Somando 438 a um número:", somar(438))

#                                              Documentação de funções (docstrings)
# É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.

# def area_retangulo(base, altura):
#     """
#     Calcula a área de um retângulo.

#     Args:
#         base (float): A base do retângulo.
#         altura (float): A altura do retângulo.

#     Returns:
#         float: A área do retângulo.
#     """
#     return base * altura

#                                               Funções com número variável de argumentos
# Python permite definir funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador * antes do nome do parâmetro.
    
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22

