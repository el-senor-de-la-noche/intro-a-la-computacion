contador = 0
nombres = []
claves = []
precios = []
while contador < 4:
    nombre = input('Nombre: ')
    clave = input('Clave: ')
    precio = int(input('Precio: '))
    nombres.append(nombre)
    claves.append(clave)
    precios.append(precio)
    contador = contador + 1
descuentos = []

contador = 0
while contador < 4:
    if claves[contador] == '01':
        final = precios[contador] - precios[contador] * 0.1
    else:
        final = precios[contador] - precios[contador] * 0.2
    descuentos.append(final)
    contador = contador + 1

contador = 0
while contador < 4:
    print(nombres[contador], claves[contador], precios[contador], descuentos[contador])
    contador = contador + 1

