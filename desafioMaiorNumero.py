# Faça um programa que leia 5 números e informe o maior número.
# append = adicionar

numeros = []
texto = []
numero = input('Insira o número: ')
numeros.append(numero)
textoss = 1

texto.append(textoss)

while len(numeros) < 5:
    numero = input('Insira o número: ')
    numeros.append(numero)
    textoss += 1
    texto.append(textoss)
    

print('Esse é o maior número: ' + max(numeros))


