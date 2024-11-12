contador = 0
while contador < 10:
    print('----> Iniciando transaccion ', contador + 1, ' -!-!-!-!')
    nombre = input('Nombre: ')
    clave = input('Clave: ')
    precio = int(input('Precio: '))
    if clave == '01':
        descuento = precio * 0.1
    else:
        descuento = precio * 0.2
    precio_final = precio - descuento
    print ('Precio final: ', precio_final)
    print('----> Finalizando Transaccion ',contador + 1, '-!-!-!-!')
    print()
    contador = contador + 1
print ('Fin ……')
