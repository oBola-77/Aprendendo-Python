#  IF
# A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira
idade = 25

if idade >= 18:
    print("Maior de idade")

# # IF-ELSE
# # A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa.

idade = 13

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#IF-ELIF-ELSE
# A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos.

nota = 6

if nota >= 9:
    print("O cara é mt bom")
elif nota >= 8:
    print("o caba é bom mas n é bombom, mas ainda sim é bom")
elif nota >= 7:
    print("é... nao tava mt bom, agr parece que piorou")
else:
    print("Melhore!")

idade = 17

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 60:
    print("Adulto")
elif idade == 60:
    print("Parabens")
else:
    print("Idoso")