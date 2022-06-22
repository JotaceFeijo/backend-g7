contador = 1

while contador<6:
    numLoteria = int(input('Ingrese el {} valor '.format(contador)))
    if not(numLoteria>100 or numLoteria<0):
        contador = contador + 1
        continue
    print('número ingresado es inválido, vuelva a intentar')



    