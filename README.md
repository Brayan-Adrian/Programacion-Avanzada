# Tecnologico de Estudios Superiores de Huixquilucan
### Ingenieria Mecatronica
### Asignatura: Programación avanzada
### Asesor. Dr. Enrique García Trinidad
### Alumno. Brayan Adrian Navarrete Maltos

### Plataforma python
### Que es python?
Python es un lenguaje de programación creado por Guido van Rossum a principios de los años 90. 
El programa favorece una sintaxis muy limpia ya que favorece un codigo legible. Se trata de un lenguaje interpretado o de script, con tipado dinamico, fuertemente tipado, multiplatoforma orientada a objetos.

### Lenguaje interpretado o de Script
Un lenguaje interpretado o de Script es aque que se ejecuta utilizando un programa de intermedio llamado interprete, en lugar de compilar el codigo al lenguaje maquina que puede comprender y ejecutar directamente la computadora "Lenguajes compilados".
La ventaja de los lenguajes compilados es que en su ejecución es más rápida.
Sin embargo, los lenguajes interpretados son más flexibles y más portátiles. Python es un ejemplo de un lenguaje de alto nivel como C ++, C #, PHP, Pascal y Java, los idiomas de alto nivel se consideran los lenguajes maquina o lenguajes de ensamblador sin embargo, los idiomas de alto nivel simpre tienen que ser convertidos a lenguajes de bajo nivel poara que puedan correr.
El lenguaje de programacion python guarda sus scripts en terminacion archivo.py

### Tipado dinamico
La caracteristica de tipado dinamico  a que no es necesario declarar  el tipo de dato que va a contener una determinada variable  si no que segun su tipo  de valor al que se le asigne y al tipo de esta variable puede cambiar si se le asigna un valor de otro tipo.

### Fuertemente tipado 
No se pertmite tratar una variable  como si fuera de un tipo distinto al que tiene es necesario convertir de forma explicit dicha variable al nuevo tipo previamente .
Ejemplo: Si tenemos una variable que contiene un texto 1 variable de tipo cadena o string 1 no podemos tratarlo como un numero 1 sumar la cadena "9"+8.

### Multiplataforma 
El interprete de python esta disponible en multitud de plataformas  (UNIX, SOLARIS , LINUX, DOS , WINDOWS, MAC OS) Por lo tanto si noutilizamos librerias especificas de esta plataforma nuestro programa podra correr  en estos sistemas sin grandes cambios 

### Orientada a objetos
La orientacion a objetos es un paradigma de programacion en el que los conceptos del mundo real relevantes para nuestro problema se trasladan a clases y objetos en nuestro programa la ejecucion del programa consiste en una serie de interacciones entre los objetos .

### Por que python ?
El software es el nucleo de todas las herramientas que utilizamos hoy en dia casi todos usamos redes sociales para comunicarnos muchaspersonas estan conectadas a internet todo el dia , y la mayoria de los trabajos siempre se interactuan con una computadora o para tener el trabajo hecho. Como resultado la demanda de las personas que sepan programar a aumentado .
Python es un lenguaje que con su sintaxis simple, clara y sencilla puede automatizar simples tareas como mover, nombrar o reciclar archivos, llenar de forma automatica formularios en internet, descargar archivos o extraer informacion de paginas de internet de forma masiva, hace que su computadora le envie a su telefono informacion de quien la esta usando , checar su email y contestarlo de manera automatica.

Para poder programar en python es necesario instalar su programa lo cual es muy facil solo hay que ir a la pagina ANACONDA PYTHON y descargar la  version  3.7 para 64 bits es de gran importancia señalar el sistema  en el cual lo vamos a trabajar, ya instalado el programa procederemos a la programacion y para ello en el buscador del sistema indicamos la palabra spyder ya que este es el programa donde haremos todos nuestros programas.

Programa No.1 
El comando print imprime un mensaje en la pantalla o en otro dispositivo de salida. El mansaje puede ser una cadena de caracteres o cualquier objeto que sea convertible a cadena de caracteres. 
El comando del programa es el siguiente: https://github.com/Brayan-Adrian/Programacion-Avanzada/blob/master/Ej1%20Cual%20es%20tu%20nombe.py
Y tambien lo podemos ver en la siguinete imagen.
<img src="1 py.png" />

Programa No.2
El comando print imprime un mensaje en la pantalla o en otro dispositivo de salida. El mansaje puede ser una cadena de caracteres o cualquier objeto que sea convertible a cadena de caracteres. 
El comando input permite al usuario introducir informacion utilizando el teclado la variable donde se guarda dicha informacion es de tipo string o cadena de caracteres.
El comando int convierte a tipo entero.
El comando float convierte a tipo decimal.
El comando del programa es el siguiente:https://github.com/Brayan-Adrian/Programacion-Avanzada/blob/master/Ej2%20Nombre%2C%20edad%2C%20estatura.py
Y tambien lo podemos ver en la siguinete imagen.
<img src="Ej2 Nombre, Estatura, Edad.png" /> 

Programa No.3
Escribe un programa que desplieje su nombre y su direccion de tal manera que pueda escribir en un sobre de correo , su programa no tiene que leerningun dato de entrada por el usuario.
En este programa solo se utilizara el comando print ya que solo requiere que imprima el mensaje en el sobre de la carta, a continuacion se presenta el codigo programado de lado izquiero y del lado derecho la compilacion.
<img src="1 py.png" />

Programa No.4
Escriba un programa que le pregunte al usuario el largo y el anchode una habitacion. Una vez que los valore han sido leidos su programa debe calcular y desplegar el area de la habitacion. El largo y el ancho debe de ser introducido con punto flotante (decimal) Incluya las unidades metros en su mensaje de estrada y de salida.
<img src="2 py.png" />

Programa No.5
Crea un programa que lea el largo y ancho de un campo de cultivo, introducido por el usuario y despliege el area del campo en acres
<img src="3 py.png" />

Ejercicio de tarea No.6

En muchos establecimientos, se agrega un pequeño depósito a los envases de bebidas para alentar a las personas a reciclarlos. En una jurisdicción en particular, los envases de bebidas con un litro o menos tienen un depósito de $0.10, y los envases de bebidas con más de un litro tienen un depósito de $ 0.25.
Escriba un programa que lea el número de contenedores de cada tamaño del usuario. Su programa debe continuar calculando y mostrando el reembolso que se recibirá por devolver esos contenedores. Formatee la salida para que incluya un signo de dólar y siempre muestre exactamente dos decimales.

Solucion: hay que resaltar que solo nos estan pidiendo dos decimales para eso se utilizara el siguiente codigo "$%.2f' %" a la hora de que muestre el resultado de la operacion, las variables de las botellas a introducir seran de tipo en tero ya que no podemos introducir decimales en dicha orden, y la operacion del rembolso se realiza multiplicando las botellas ya sean chicas o grandes por la variable establecida, y despues sumar las dos variables, para que quede mejor entendible se presentara a continuacion el siguiente codigo. https://github.com/Brayan-Adrian/Programacion-Avanzada/blob/master/EjTarea.py
Y tambien lo podemos ver en la siguinete imagen.
<img src="Ej2Tarea.png" />

Programa No.7
Escriba un programa que lea un numero positivo (n), insertado por el usuario y despues despliege la suma de todos los enteros desde 1 hasta n. La suma de los primeros enteros n positivos puede ser calculado usando la formula suma=(n)(n+1)

Solucion. Insertamos un numero cualquiera, en este caso se eligio 5 ya que es el mas facil de comprobar y calcularlo mentalmente, la formua se muestra en la parte de arriba, el codigo es el siguiente. https://github.com/Brayan-Adrian/Programacion-Avanzada/blob/master/Ej7.py
<img src="Ej7 inserta un numero positivo.png" />

Programa No.8
Hacer un programa en el que el usuario introduzca el nombre de la comida que ordeno en un restaurante y su precio despues su programa debe calcular el subtotal, el iva y la propina, de toda la cuenta la salida del programa debe parecerse a un ticket de restaurante. Use un iva de 16% y una propina del 15% del subtotal. Los valores numericos deben tener dos decimales.

Solucion. Para poder llegar al objetivo de lo indicado pondremos el nombre y el valor de 5 comidas, con el comando print seguido de str haremos el nombre de la comida y con el valor de la comida de igual forma el comando print seguido del comando int. crearemos las varibles Subtotal, IVA, Propina para poderlas sumar y muestre al final el monto total, el codigo es el siguiente.
https://github.com/Brayan-Adrian/Programacion-Avanzada/blob/master/Ej6%20Ticket.py
Y tambien lo podemos ver en la siguiente imagen.
<img src="Ej6 Ticket.png" />

Programa No.9
Un vendedor de una pagina de abarrotes en linea vende dos tipos de cajas de cereal. CornFlakes de 750gr y Trix de 500gr. Escriba un programa que lea el numero de cajas de CornFlakes y cajas de Trix, cuyo valor debe ser introducido por el usuario. Despues, su programa debe calcular y mostrar el total del peso (en kilogramos).

Solucion. Empezamos agregando las constantes T, y C de las cajas ya que son los gramos que pesa cada una, y las multiplicamos por las variables que van hacer el numero que el usuario introducira.
Hacemos una variable que haga la operacion de sumar los gramos por las cajas a introducir y las dividimos entre 1000 para que nos imprima los kilogramos, el codigo es el siguiente.https://github.com/Brayan-Adrian/Programacion-Avanzada/blob/master/Ej8%20Peso%20de%20las%20cajas.py
Y tambien lo podemos ver en la siguiente imagen.
<img src="Ej8 Peso de Cajas.png" />

Programa de tarea No.10 Aritmetica
Cree un programa que lea dos valores enteros, a y b, introducidos por el usuario. Su programa debe desplegar la suma de a y b 
La diferencia cuando a es sustraido de b 
El cociente cuando a divide a b
El residuo cuando a divide a b 
El resultado de log(a)
El resultado de a a la potencia b 

Solucion. Un tip a utilizar es mandando a llamar la libreria Math la cual no ubicaremos en la parte de abajo de la plataforma spyder y pondremos import math seguido de comando enter para que nos despliege la lista de funciones matematicas, el codigo es el siguiente.https://github.com/Brayan-Adrian/Programacion-Avanzada/blob/master/Aritmetica.py
Y tambien lo podemos ver en la siguiente imagen.<img src="Aritmeticaa.png" />

Programa de tarea No.11 Eficiencia de combustible
En los Estados Unidos, la eficiencia del combustible para vehículos se expresa normalmente en millas por galón (MPG). En México, la eficiencia del combustible normalmente se expresa en litros por cien kilómetros (L / 100km). Usa tus habilidades de investigación para determinar cómo convertir de MPG a L / 100km. Luego, cree un programa que lea un valor del usuario en unidades estadounidenses y muestre la eficiencia de combustible equivalente en unidades mexicanas.

Solucion para poder convertir de MPG a L/100km es hacer la siguiente conversion multiplicar el numero introducido por 1.609 millas y despues dividirlo entre 3.78 que es lo que equivale a un galon, el codigo es el siguiente.
Y tambien lo podemos ver en la siguiente imagen.<img src="Eficiencia de combustible.png" /




