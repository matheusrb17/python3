#desconto de preço de produto

preco = float(input('Informe o preço do produto: '))
calculo = (5/100)*preco
desconto = preco - calculo
print('Seu produto custava R${}. Agora, com 5 porcento de desconto, ele custa R${}.'.format(preco, desconto))
