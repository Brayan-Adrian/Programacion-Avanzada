lado1=float(input('ingrese la medida del lado 1: '))
lado2=float(input('ingrese la medida del lado 2: '))
lado3=float(input('ingrese la medida del lado 3: '))

if lado1==lado2 and lado2==lado3:
    print('Es un triangulo Equilatero')
elif lado1==lado2 or lado2==lado3 or lado3==lado1:
    print('Es un triangulo Isoceles')
else:
    print('Es un triangulo Escaleno')