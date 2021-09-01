# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.

nota = int(input('Nota entre 0 e 10: '))

if nota > 0 and nota < 10:
     print('Sua nota é ' + str(nota))

while nota > 10 or nota < 0:
    print('Favor inserir um número válido!')
    nota = int(input('Nota entre 0 e 10: '))
    if nota > 0 and nota < 10:
     print('Sua nota é ' + str(nota))

   
    


