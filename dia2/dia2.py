from ast import If


numeros = [10,20,30,40,50,60]
longNumeros = len(numeros)
for numero in numeros:
    print(numero)
fraseMotivadora = 'A quién madruga, encuentra todo cerrado'
contador = 0
for caracter  in fraseMotivadora:
    if caracter == 'n':
        contador = contador + 1
print('Hay {} veces repetidas la letra n'.format(contador))

# manual
# for i in range(valor1) imprimirá desde 0 hasta un numero menor del valor1
# for i in range(valor1, valor2) imprimirá desde el valor1 hasta un número antes de valor2
# for i in range(valor1, valor2, valor3) el tercer valor3 es de cuanto en cuanto
for i in range(3,10):
    print(i)

ejemplo2 = [10,30,12,17,24,67]
contador1 = 0
contador2=0
for numPar in ejemplo2:
    if (numPar % 2 ==0 and numPar % 3 == 0):
        contador1=contador1+1
print('hay {} numeros que son pares y multiplo de 3'.format(contador1))

for valor in range(0,20):
    if valor==5:
        print('el usuario fue encontrado')
        # el break sirve para finalizar de manera prematura
        continue
    print(valor)

Alumnos = ['Daniel', 'Jhonathan','John','Pablo']
for alumno in Alumnos:
    if alumno == 'Pablo':
        print('Alumno se encuentra en la relación')
        break
else:
    print('Alumno no se encuentra en la relación')




    