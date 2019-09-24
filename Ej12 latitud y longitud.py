#Ejercico 12 Distancia entre dos puntos de la tierra.
#La superficie de la tierra es cuerva y la distancia entre grados de longitud varia con la latitud.
#Como resultado, encontrar la distancia entre dos puntos de la superficie de la tierra es mas complicado que usar el teorema de pitagoras
#Si (t1,g1) y (t2,g2) es la latitud y longitud de dos puntos de la superficie de la Tierra. La distancia entre, esos puntos atraves de la superficie de la tierra,
#en kilometros es;

#distancia=6371.01*arccos(sen(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2))

#Cree un programa que le permita al usuario introducir la latitud y longitud de dos puntos de la tierra en grados 
#Su programa debe pesplejar la distancia entre esos puntos, en kilometros. Tenga en cuenta que las funciones 
#trigonometricas en python trabajan en radianes, por lo que debe de convertir el valor introducido por el usuario en grados
#a radianes antes de utilizar la formula. El modulo math contiene el comando radians, que cambia de grados a radianes.
 
import math

t1=int(input('introduce el punto inicial de latitud'))
t2=int(input('introduce el punto final de latitud'))
g1=int(input('introduce el punto inicial de longitud'))
g2=int(input('introduce el punto final de longitud'))

lat1=(math.pi*(t1))/180
lat2=(math.pi*(t2))/180
log1=(math.pi*(g1))/180
log2=(math.pi*(g2))/180

dis=6371.01*math.acos(math.sin(lat1)*math.sin(log1)+math.cos(lat1)*math.cos(log1)*math.cos(lat2-log2))

print('La distancia es',dis,'km')


