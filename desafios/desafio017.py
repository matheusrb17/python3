import math
catOp = float(input('Informe o CATETO OPOSTO: '))
catAdj = float(input('Informe o CATETO ADJACENTE: '))
calculo = catOp*catOp + catAdj*catAdj
hipotenusa = math.sqrt(calculo)
print('A hipotenusa é igual a: {:.2f}'.format(hipotenusa))
