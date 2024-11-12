contador = 0
lista = []
while contador < 4:
    nombre = input('Nombre: ')
    clave = input('Clave: ')
    precio = int(input('Precio: '))
    lista.append([nombre, clave, precio])
    contador = contador + 1
print(lista)
