#quantidade de tinta necessária

largura = float(input('Insira a LARGURA, em metros, da sua parede: '))
altura = float(input('Insira a ALTURA, em metros, da sua parede: '))
area = largura * altura
litros = area / 2
print('Sua parede tem uma área de {} metros quadrados e necessita de {} litros para que seja pintada.'.format(area, litros))
