#Ej 46 
#El año esta dividido en e cuatro tempradas: primera, invierno, verano o otoño
#Aunque las fechas exactas cambian un poco dependiendo del año, usemos las siguientes fechas:

#Temporada Ptimer Dia

#Primavera Marzo 21
#Verano    Junio 21
#Otoño     Septiembre 22
#Invierno  Diciempbre 21

#Escriba un programa en el que el usuario introduzca el mes y el dia. El usuario 
#introduzca el nombre del mes como una string seguido del dia como un entero "int".
#Su programa debe desplegar la temporada de acuerdo a la informacion introducida por el ususario

mes=str(input('Introduce el mes'))
dia=int(input('Introduce el dia'))


if mes=='Enero' or mes=='Febrero':
    temporada='Invierno'
elif mes=='Marzo' and dia<20:
    temporada='Invierno'
elif mes=='Marzo' and dia>=21:
    temporada='Primavera'
elif mes=='Abril' or mes=='Mayo':
    temporada='Verano'
elif mes=='Junio' and dia<20:
    temporada='Verano'
elif mes=='Julio' or mes=='Agosto':
    temporada='Otoño'
elif mes=='Septiembre' and dia<22:
    temporada='Otoño'
elif mes=='Octubre' or mes=='Noviembre':
    temporada='Invierno'
elif mes=='Diciembre' and dia<21:
    temporada='Invierno'
else:
    print('La temporada es',str(temporada))

