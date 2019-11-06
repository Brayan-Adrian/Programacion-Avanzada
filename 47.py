#Los horóscopos comúnmente reportados en los periódicos usan la posición del sol en el
#momento del nacimiento para intentar predecir el futuro. Este sistema de astrología divide el
#año en doce signos del zodiaco, como se describe en la tabla a continuación:
#Escriba un programa que le pida al usuario que ingrese su mes y día de nacimiento. Entonces
#su programa debe informar el signo del zodiaco del usuario como parte de una salida adecuada
#mensaje.

dia=int(input('Ingresa el dia'))
mes=str(input('ingresa el mes'))

if dia>=20 and mes=="enero":
    print('Tu signo es acuario')
elif dia<=18 and mes=="febrero":
    print('Tu signo es acuario')

elif dia>=19 and mes=="febrero":
    print('Tu signo es picis')
elif dia<=20 and mes=="marzo":
    print('Tu signo es picis')

elif dia>=21 and mes=="marzo":
    print('Tu signo es aries')
elif dia<=19 and mes=="abril":
    print('Tu signo es aries')

elif dia>=20 and mes=="abril":
    print('Tu signo es tauro')
elif dia<=20 and mes=="mayo":
    print('Tu signo es tauro')

elif dia>=21 and mes=="mayo":
    print('Tu signo es geminis')
elif dia<=20 and mes=="junio":
    print('Tu signo es geminis')
    
elif dia>=21 and mes=="junio":
    print('Tu signo es cancer')
elif dia<=22 and mes=="julio":
    print('Tu signo es cancer')

elif dia>=23 and mes=="julio":
    print('Tu signo es leo')
elif dia<=22 and mes=="agosto":
    print('Tu signo es leo')
    
elif dia>=23 and mes=="agosto":
    print('Tu signo es virgo')
elif dia<=22 and mes=="septiembre":
    print('Tu signo es virgo')
    
elif dia>=23 and mes=="septiembre":
    print('Tu signo es libra')
elif dia<=22 and mes=="octubre":
    print('Tu signo es libra')

elif dia>=23 and mes=="octure":
    print('Tu signo es escorpio')
elif dia<=21 and mes=="noviembre":
    print('Tu signo es escorpio')

elif dia>=22 and mes=="noviembre":
    print('Tu signo es sagitario')
elif dia<=21 and mes=="diciembre":
    print('Tu signo es sagitario')
    
elif dia>=22 and mes=="diciembre":
    print('Tu signo es capricornio')
elif dia<=19 and mes=="enero":
    print('Tu signo es capricornio')
    
else:
    print('fecha incorrecta')
