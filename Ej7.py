#Escriba un programa que lea un numero positivo (n), insertado por el usuario
#y despues despliege la suma de todos los enteros desde 1 hasta n. La suma de  
#los primeros enteros n positivos puede ser calculado usando la formula
#suma=(n)(n+1)

n=int(input('Inserta un numero positivo'))
tot=(n*(n+1))//2

print('la suma de todos los numeros enteros es'+ str(tot))
