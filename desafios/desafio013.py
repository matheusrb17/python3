#aumento de salário

salario = float(input('Informe seu salário: '))
calculo = (15/100)*salario
novoSalario = salario + calculo
print('Seu salário era R${}, com aumento de 15 porcento, atualiza para R${}'.format(salario, novoSalario))
