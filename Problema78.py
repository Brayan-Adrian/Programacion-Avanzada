#Escriba un programa que convierta un número decimal (base 10) a binario (base 2). Leer el
#número decimal del usuario como un entero y luego use el algoritmo de división que se muestra
#a continuación para realizar la conversión. Cuando se completa el algoritmo, el resultado contiene el
#Representación binaria del número. Mostrar el resultado, junto con un
#mensaje.
#Deje que el resultado sea una cadena vacía
#Deje que q represente el número a convertir
#repetir
#Establezca r igual al resto cuando q se divide por 2
#Convierta r en una cadena y agréguela al comienzo del resultado
#Divida q entre 2, descartando cualquier resto, y almacene el resultado nuevamente en q
#hasta q es 0

Base=2
num=int(input('Introduzca el numero a convertir'))
result=''
q=num
r=q%Base
result=str(r)+result
q=q//Base

while q>0:
    r=q%Base
    result=str(r)+result
    q=q//Base

print('en numero binario es',result)