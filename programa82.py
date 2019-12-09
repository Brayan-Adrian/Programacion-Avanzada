# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:54:12 2019

@author: stitch
"""

#programa 82
#En la ciudad de mexico l atarifa de taxi uber consiste en un precio base de 44 pesos mas 12 pesos por cada
#km recorrido. Escriba una funcion que tome la distancia viajada(km) elc ual debe ser el unico argumento
#y regrese la tarifa total como resultado. Exriba un prorama principal que demuestre la funcion

def tarifa(distancia):
    total=44.00+distancia*12.00
    return total

dist=float(input('Ingrese la distancia(km): '))
cuota=tarifa(dist)

print(cuota)