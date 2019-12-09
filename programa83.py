
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:07:41 2019

@author: stitch
"""

#Amazon provee envio express para muchos de sus productos a un costo de 195 pesos por el primer producto
#IDE 29.50 para cada producto subsecuente. Escriba una funcion que tome el numero de productos como
#su unico argumento. Regrese el costo de envio total como el resultado de la funcion.
#Incluya un programa principal que lea el numero de productos comprados por el usuario y que despliegue el 
#costo total de envio.

def envio(produc):
  
   if produc==1:
       total=195  
   elif produc >= 2:
       total=195+(29.50*(produc-1))
       
   return total

num=int(input('Ingrese el numero total de productos: '))
envit=envio(num)
print('El total de los prooductos es:', envit)
