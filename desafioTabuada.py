tabuada = int(input('Insira o número que você deseja ver a tabuada: '))
vezes = 0

print('Tabuada de ' + str(tabuada) +':')
while vezes < 10:
    vezes += 1
    print('5 X ' + str(vezes), end=" = ")
    print((tabuada * vezes)) 
