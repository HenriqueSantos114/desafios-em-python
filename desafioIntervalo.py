# Faça um programa que receba dois números inteiros e gere os números inteiros que 
# estão no intervalo compreendido por eles.

nmr1 = int(input('Insira um número: '))
nmr2 = int(input('Insira o segundo número: '))
numeros = []
if nmr1 < nmr2:
    while nmr1 != nmr2:
        nmr1 += 1
        numeros.append(nmr1)
        print(nmr1)
       
else:
    while nmr2 != nmr1:
        nmr2 += 1
        numeros.append(nmr2)
        print(nmr2)
        
print('Há um intervalo de ' + str(len(numeros)) +' entre os dois valores inseridos (menor: ' + str(min(numeros)) + ' maior: ' + str(max(numeros)) + ')')

