                                            # Try
# O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")

                                            # Except
# O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.

try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

                                            # Finally
# O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

try:
    arquivo = open("arquivo.txt", "r")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()