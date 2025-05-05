# For
# O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável

print("Numeros de 1 a 5 multiplicados por 2 com for")
for numero in range(1, 6):
    print(numero*2)

# While
# O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira.

print("\nNuemros de 1 a 5 multiplicados por 2 com while")
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Break
# A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição. Quando um break é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop.

print("\nUsando o controle de loop break")
contador = 0
while True:
    print(contador)
    contador += 1
    
    if contador == 20:
        break
    
#Neste exemplo, o loop while é executado indefinidamente devido à condição True. No entanto, dentro do loop é utilizada uma estrutura condicional if para verificar se contador é igual a 5. Quando essa condição é satisfeita, a instrução break é executada, fazendo com que o loop seja interrompido e o fluxo de execução continue com a próxima instrução fora do loop.
    
# Continue
# A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração

print("\nUsando o controle de loop Continue")
for i in range (10):
    if i % 2 == 0:
        continue
    print(i)
    
#Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado, apenas os números ímpares serão impressos.


    
# Pass
# A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

print("\nUsando o controle de loop Pass")
for i in range(5):
    pass

#Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.

