from math import radians, sin, cos, tan
a = float(input('Digite um ângulo: '))
seno = sin(radians(a))
print('O valor do seno {} é {:.3f}' .format(a, seno))
cos = cos(radians(a))
print('O valor do cosseno {} é {:.3f}'.format(a, cos))
tan = tan(radians(a))
print('O valor da tangente {} é {:.3f}'.format(a, tan))
