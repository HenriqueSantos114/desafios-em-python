# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.
 
imprima = int(0)

while imprima <= 19:
    imprima += 1
    print('Número: ' + str(imprima))

while imprima <= 19:
    imprima += 1
    print(str(imprima) + ',', end="")