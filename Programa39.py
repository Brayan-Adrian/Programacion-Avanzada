nivel=int(input('Ingrese el nivel del sonido: '))

if nivel<=40:
    print('Muy bajo')
elif nivel>40 and nivel<=70:
    print('Bajo')
elif nivel>70 and nivel<=106:
    print('Fuerte')
elif nivel>106 and nivel<=130:    
    print('Muy fuerte')
elif nivel>130:
    print('Excesivamente fuerte')
else:
     print('Opcion invalida')
