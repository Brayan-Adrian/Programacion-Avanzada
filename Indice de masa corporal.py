##Indice d emasa corporal
masa=float(input('Inserta tu masa en kilogramos'))
estatura=float(input('Inserta la estatura en metros'))

imc=masa/(estatura)**2

if imc<16:
    print('Tiene delgadez severa')
elif imc>=16 and imc<17:
    print('Tienes delgadez moderada')
elif imc>=17 and imc<18.5:
    print('Tienes delgadez leve')
elif imc>=18.5 and imc<25:    
    print('Tienes delgadez leve')
elif imc>=25 and imc<30:
    print('Tienes preobesidad')
elif imc>=30 and imc<35:
    print('Tienes preobesidad')
elif imc>=35 and imc<40:
    print('Tienes obesidad media')
elif imc>=40:
    print('Tienes obesidad morbida')
else:
     print('Opcion invalida')

print('su IMC fue de', imc)
    
    
    

    

    