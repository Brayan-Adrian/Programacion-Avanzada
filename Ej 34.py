#Escriba un programa que lea un numero entero introducido por el usuario.
#Su programa debe desplegar un mensaje indicando si su numero entero es par o impar.

num=int(input('ingresa un numero'))

if num % 2 == 1:
    print('Es un numero impar',num)
else:
    print('Es un numero par',num)