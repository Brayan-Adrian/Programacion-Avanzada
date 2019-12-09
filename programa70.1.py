# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:05:59 2019

@author: stitch
"""

mensaje=input('ingresa el cifrado: ')
cambio=2
nvmen=""
for ch in mensaje:
    if ch>="a" and ch<="z":
      pos=ord(ch)-ord('a')
      pos=(pos-cambio)%26
      newcara=chr(pos+ord('a'))
      nvmen=nvmen+newcara
    elif ch>='A' and ch <='Z':
      pos=ord(ch)-ord('A')
      pos=(pos-cambio)%26
      newcara=chr(pos+ord('A'))
      nvmen=nvmen+newcara
    else:
      nvmen=nvmen+ch
    
print('El mensaje decifrado es: ', nvmen)
    