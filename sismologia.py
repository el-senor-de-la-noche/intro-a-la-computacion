import matplotlib.pyplot as plt

def lee_datos(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split()
        datos.append(lista)
    ent.close()
    return datos

def funcion_a(datos):
    mayor = 0
    for lista in datos:
        if float(lista[4]) > mayor:
            mayor = float(lista[4])
            fecha = lista[0]
            hora = lista[1]
    return [fecha, hora]

def funcion_b(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 7 and float(lista[4]) < 8:
            contador = contador + 1
    return contador

def funcion_c(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 8 and float(lista[4]) < 9:
            contador = contador + 1
    return contador

def funcion_d(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 9:
            contador = contador + 1
    return contador

def funcion_e(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if float(fecha[2]) < 1600:
            contador = contador + 1
    return contador

def funcion_f(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if float(fecha[2]) >= 1600 and float(fecha[2]) < 1700:
            contador = contador + 1
    return contador

def funcion_g(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if float(fecha[2]) >= 1700 and float(fecha[2]) < 1800:
            contador = contador + 1
    return contador

def muestra_datos(resp_a, resp_b, resp_c, resp_d, resp_e, resp_f, resp_g):
    print("Fecha:", resp_a[0]," y hora:", resp_a[1],"del mayor sismo registrado.")
    print()
    print("Cantidad de sismos >= 7.0 y < 8.0:", resp_b)
    print()
    print("Cantidad de sismos >= 8.0 y < 9.0:", resp_c)
    print()
    print("Cantidad de sismos >= 9.0:", resp_d)
    print()
    print("Cantidad de sismos siglo 16:", resp_e)
    print()
    print("Cantidad de sismos siglo 17:", resp_f)
    print()
    print("Cantidad de sismos siglo 18:", resp_g)
    print()

def graficar(resp_e, resp_f, resp_g):
    x = [16, 17, 18]
    y = [resp_e, resp_f, resp_g]
    plt.bar(x, y)
    plt.show()

if __name__ == "__main__":
    datos = lee_datos('terr.txt')
    resp_a = funcion_a(datos)
    resp_b = funcion_b(datos)
    resp_c = funcion_c(datos)
    resp_d = funcion_d(datos)
    resp_e = funcion_e(datos)
    resp_f = funcion_f(datos)
    resp_g = funcion_g(datos)
    muestra_datos(resp_a, resp_b, resp_c, resp_d, resp_e, resp_f, resp_g)
    graficar(resp_e, resp_f, resp_g)