def lee_datos(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        datos.append(linea.rstrip('\n').split(','))
    ent.close()
    return datos

def sobrevivientes(datos):
    cantidad = 0
    for persona in datos:
        if persona[1] == '1':
            cantidad = cantidad + 1
    return cantidad

def mujeres(datos):
    cantidad = 0
    for persona in datos:
        if persona[3] == 'female':
            cantidad = cantidad + 1
    return cantidad

def mujeres_sobreviven(datos):
    cantidad = 0
    for persona in datos:
        if persona[3] == 'female' and persona[1] == '1':
            cantidad = cantidad + 1
    return cantidad

def primera_sobreviven(datos):
    cantidad = 0
    for persona in datos:
        if persona[0] == '1' and persona[1] == '1':
            cantidad = cantidad + 1
    return cantidad

def tercera_sobreviven_h(datos):
    cantidad = 0
    for persona in datos:
        if persona[0] == '3' and persona[1] == '1' and persona[3] == 'male':
            cantidad = cantidad + 1
    return cantidad

def muestra_datos(sobreviven, women, women_s, primera_s, tercera_s_h):
    print('Sobreviven: ', sobreviven)
    print('Mujeres: ', women)
    print('Mujeres sobreviven: ', women_s)
    print('Primera sobreviven: ', primera_s)
    print('Tercera hombres sobreviven: ', tercera_s_h)


if __name__ == '__main__':
    datos = lee_datos('titanic3_nuevo.txt')
    sobreviven = sobrevivientes(datos)
    women = mujeres(datos)
    women_s = mujeres_sobreviven(datos)
    primera_s = primera_sobreviven(datos)
    tercera_s_h = tercera_sobreviven_h(datos)
    muestra_datos(sobreviven, women, women_s, primera_s, tercera_s_h)