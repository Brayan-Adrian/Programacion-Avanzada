# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:25:12 2019

@author: stitch
"""

#ejersicio 81
#Escribir una funcion que tome la longitud de los dos lados mas cortos de un triangulo rectangulo como
#argumentos. La funcion debe de regresar la hipotenusa del triangulo calculado usando el teorema de 
#pitagoras como resultado de la funcion. Incluya un programa principal que lea las longitudes 
#usando la funcion para calcular la longitud de la hipotenusa y que tambien se despliegue el resultado

def calcular_hipotenusa(lado1,lado2):
    hipotenusa=(lado1**2+lado2**2)**(1./2.)
    return hipotenusa

l1=float(input('Inserta el valor dde lado1: '))
l2=float(input('Inserta el valor dde lado2: '))

hip=calcular_hipotenusa(l1,l2)
hip2=calcular_hipotenusa(3.5,5.0)
hip2=calcular_hipotenusa(8.2,6.0)

print('La hipotenusa es: ', hip)


