#Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
#de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
    if i == 0 or i == altura-1:
        print("#" * largura)
    else:
        print("#" + " " * (largura-2) + "#")
