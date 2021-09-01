# Supondo que a população de um país A seja da 
# ordem de 80000 habitantes com uma taxa anual de crescimento de 
# 3% e que a população de B seja 200000 habitantes com uma taxa de 
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
# necessários para que a população do país A ultrapasse ou iguale a população do país B, 
# mantidas as taxas de crescimento.


# 80000 = A CADA ANO É 1.030 
# 200000 = A CADA ANO É 1.015

letraA = 80000
letraB = 200000
anos = 0
  
while letraA <= letraB:
    letraA *= 1.030
    letraB *= 1.015
    anos += 1

print('Para que a população A, passe ou iguale a população B deverá passar no mínimo: ' + str(anos) + ' anos')