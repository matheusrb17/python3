import math
num = float(input('Informe um ângulo qualquer: '))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O ângulo de {} tem o SENO de {:.2f}'.format(num, seno))
print('o ângulo de {} tem o COSSENO de {:.2f}'.format(num, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(num, tan))
