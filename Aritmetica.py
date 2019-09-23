# Ejercicio 10 Aritmetica
# Cree un programa que lea dos valores enteros, a y b, introducidos por el usuario.
#Su programa debe desplegar
#- La suma de a y b 
# La diferencia cuando a es sustraido a b 
# El cociente cuando a divide a b
# El residuo cuando a divide a b 
# El resultado de log(a)
# El resultado de a a la potencia b 
import math
a=int(input('Introduce el primer numero entero'))
b=int(input('Introduce el segundo numero entero'))

suma=a+b
resta=a-b
division=a/b
residuo=a%b
log=math.log(a)
potencia=a**b

print('suma %.2f' % suma)
print('resta %.2f' % resta)
print('division %.2f' % division)
print('residuo %.2f' % residuo)
print('log %.2f' %log)
print('potencia %.2f' % potencia)



