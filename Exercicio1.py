#Escreva um programa que recebe como entradas (utilize a função input) 
#dois números inteiros correspondentes à largura e à altura de um retângulo, 
#respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), 
#uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
    linha = ""
    for j in range(largura):
        linha += "#"
    print(linha)
