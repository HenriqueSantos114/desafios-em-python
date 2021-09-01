# Faça um programa que leia 5 números e informe a soma e a média dos números.
# sum = soma todos os valores de uma lista

numeros = []
numero = int(input('Insira sua primeira nota: '))
numeros.append(numero)

while len(numeros) < 5:
    numero = int(input('Insira sua próxima nota: '))
    numeros.append(numero)

soma = sum(numeros)
media = soma/5 #MATH: len(numeros)

print('Sua média é: ' + str(media))