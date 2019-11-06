dia=int(input('Ingresa el dia: '))
mes=str(input('ingresa el mes: '))

if dia==1 and mes=="Enero":
    print('Este dia se celebra el año nuevo')
elif dia==1 and mes=="Julio":
    print('Este dia se celebra el dia de Canada')
elif dia==25 and mes=="Diciembre":
    print('Este dia se celebra el dia de Navidad')
else:
    print('Este es un dia normal')
    