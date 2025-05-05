                                            # Entrada de dados do usuário
# Para obter informações do usuário durante a execução do programa, podemos utilizar a função input(). Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.
def nome_e_idade():
    nome = input("Insira seu nome: ")
    idade = input("Insira sua idade: ")

    print(f'Olá {nome}!')
    print(f'Você tem {idade} anos!')

def validacao_de_idade():
    idade = int(input("Insira sua idade: "))

    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")


                                            # Saída de dados
# Para mostrar informações na tela, utilizamos a função print(). Esta função recebe um ou mais argumentos e os mostra no console.
# Podemos utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.

nome = "Juan"
idade = 25

print(f"Olá, meu nome é {nome} e tenho {idade} anos")

                                     
