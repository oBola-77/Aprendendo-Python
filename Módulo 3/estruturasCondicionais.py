#  IF
# A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira
idade = 25

if idade >= 18:
    print("Ai bobão, cê ja pode ser preso hein. Fica ligeiro vacilçao!")

# # IF-ELSE
# # A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa.

idade = 13

if idade >= 18:
    print("Ai bobão, cê ja pode ser preso hein. Fica ligeiro vacilçao!")
else:
    print("Tá suave, vc é de menor")

#IF-ELIF-ELSE
# A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos.

nota = 6

if nota >= 9:
    print("Ta porra, o caba é bom memo")
elif nota >= 8:
    print("o caba é bom mas n é bombom, mas ainda sim é bom")
elif nota >= 7:
    print("é... nao tava mt bom, agr parece que piorou")
else:
    print("O caba burro da gota, mizericordia")

idade = 89

if idade < 18:
    print("Menõ de idade")
elif idade >= 18 and idade < 60:
    print("Ta mocinho já")
elif idade == 60:
    print("Parabens ai tio")
else:
    print("Ta fazendo hora extra na terra é?")