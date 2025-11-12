from random import shuffle
nome1 = str(input('Digite o PRIMEIRO nome: '))
nome2 = str(input('Digite o SEGUNDO nome: '))
nome3 = str(input('Digite o TERCEIRO nome: '))
nome4 = str(input('Digite o QUARTO nome: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem de apresentação será ')
print(lista)
