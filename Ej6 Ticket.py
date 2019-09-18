
#Ejercicio 6 Hacer un programa en el que el usuario introdusca el nombre de la comida que ordeno en un restaurante y su precio despues su programa debe calcular el subtotal, el iva y la propina, de toda la cuenta la salida del programa debe parecerse a un ticket de restaurante. Use un iva de 16% y una propina del 15% del subtotal. Los valores numericos deben tener dos decimales
I=0.16
P=0.15
A=str(input('Introduzca el nombre de la comida'))
a=float(input('Introduzca el valor de la comida'))
B=str(input('Introduzca el nombre de la comida'))
b=float(input('Introduzca el valor de la comida'))
C=str(input('Introduzca el nombre de la comida'))
c=float(input('Introduzca el valor de la comida'))
D=str(input('Introduzca el nombre de la comida'))
d=float(input('Introduzca el valor de la comida'))
E=str(input('Introduzca el nombre de la comida'))
e=float(input('Introduzca el valor de la comida'))

SubTotal=(a+b+c+d+e)
IVA=(SubTotal*I)
Propina=(SubTotal*P)
Total=(SubTotal+IVA+Propina)

print('Subtotal $%.2f' % SubTotal)
print('IVA $%.2f' % IVA)
print('Propina $%.2f' % Propina)
print('Total $%.2f' % Total)
