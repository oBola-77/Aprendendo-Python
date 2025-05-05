# Para utilizar um modulo em nosso programa, devemos importa-lo utilizando a
# declaração import. Podemos importar um módulo completo ou funções especificas
# de um módulo.
def conhecendo_math():
    import math

    resultado = math.sqrt(25)
    print(resultado)
# Neste exemplo, importa-se o módulo math utilizando a declaração import.
# Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz
# quadrada de 25.

# Tambem podemos importar funções espeficias de um módulo utilizando a sintaxe
# from modulo import função.
def conhecendo_sqrt():
    from math import sqrt

    resultado = sqrt(25)
    print(resultado)
# Neste caso, importa-se apenas a função sqrt() do módulo math, e o que nos permite
# usa-la diretamente sem ter que precedê - la com nome do módulo

                        # Funções e classes de módulos padrão
# A biblioteca de Python oferece uma ampla gama de módulos com funções e classes úteis
# Alguns exemplos incluem: Math, Random, Datetime

# Math: Fornece funções matemáticas como: sqrt() (raiz quadrada), sin() (seno)
# cos() (cosseno), entre outras

# Random: Oferece funções para gerar números aleatorios, como:
# Random () (número aleatorio entre 0 e 1), randint() (numero inteiro aleatorio em um intervalo), entre outras

# Datetime: Permite trabalhar com datas e horas, como datetime.now() (data e hora atual)
# datetime.date() (data), datetime.time() (hora), entre outras
import datetime
def conhecendo_random():
    import random
    import datetime

    numero_aleatorio = random.randint(1, 10)
    print(numero_aleatorio)
    
def conhecendo_data():
        data_atual = datetime.datetime.now()
        print(data_atual)
conhecendo_data()
