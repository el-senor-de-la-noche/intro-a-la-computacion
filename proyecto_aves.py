# Autor: Gabriel Alonso Paredes Fuentes y Daniel Navarrete Silva
import matplotlib.pyplot as plt

def lectura_datos(archivo):
    ent = open(archivo, 'r', encoding='UTF-8')
    datos = []
    for linea in ent:
        linea = linea.rstrip("\n")
        lista = linea.split(',')
        datos.append(lista)
    ent.close()
    return datos

def funcion_a(datos):
    muertes_por_region = {}
    for muerte in datos:
        region = muerte[2]
        cantidad_muertes = int(muerte[7])
        if region in muertes_por_region:
            muertes_por_region[region] += cantidad_muertes
        else:
            muertes_por_region[region] = cantidad_muertes
    return muertes_por_region

def funcion_b(datos):
    cantidad = 0
    for muerte in datos:
        if muerte[0] == "01-2023":
            cantidad += int(muerte[7])
    return cantidad

def funcion_c(datos):
    cantidad = 0
    for muerte in datos:
        if muerte[6] == "Tagua - (Columba fasciata)" and muerte[5] == "Cartagena":
            cantidad += int(muerte[7])
    return cantidad

def funcion_d(datos):
    cantidad = 0
    for muerte in datos:
        if muerte[0] == "12-02-2023" and muerte[6] == "Piquero - (Sula variegata)":
            cantidad += int(muerte[7])
    return cantidad

def funcion_e(datos):
    gaviota_garuma_muertes = 0
    piquero_muertes = 0
    gaviota_franklin_muertes = 0
    pelicano_muertes = 0
    guanay_muertes = 0

    for especie in datos:
        if especie[6] == "Gaviota garuma - (Larus modestus)":
            gaviota_garuma_muertes += int(especie[7])
        elif especie[6] == "Piquero - (Sula variegata)":
            piquero_muertes += int(especie[7])
        elif especie[6] == "Gaviota de Franklin - (Larus pipixcan)":
            gaviota_franklin_muertes += int(especie[7])
        elif especie[6] == "Pelicano - (Pelecanus thagus)":
            pelicano_muertes += int(especie[7])
        elif especie[6] == "Guanay - (Phalacrocorax bougainvillii)":
            guanay_muertes += int(especie[7])

    especies = ["Gaviota garuma - (Larus modestus)", "Piquero - (Sula variegata)", 
                "Gaviota de Franklin - (Larus pipixcan)", "Pelicano - (Pelecanus thagus)", 
                "Guanay - (Phalacrocorax bougainvillii)"]
    conteo_especies = [gaviota_garuma_muertes, piquero_muertes, gaviota_franklin_muertes, pelicano_muertes, guanay_muertes]

    plt.figure(figsize=(17, 5))
    plt.bar(especies, conteo_especies)
    plt.xlabel('Especies')
    plt.ylabel('Cantidad de muertes')
    plt.title('Cantidad de muertes por especie')
    plt.savefig("grafico_mortalidad.png")
    plt.show()
def genera_salida(muertes_region, muertes_en_enero, muertes_tagua_cartagena, muertes_piquero_12f):
    with open('resultadoS2.txt', 'w', encoding='utf-8') as salida:
        salida.write(f"Autor(es): Gabriel Alonso Paredes Fuentes y Daniel Navarrete Silva \n\n")
        salida.write("Cantidad de aves muertas por región:\n\n")
        for region, cantidad in muertes_region.items():
            salida.write(f"Nombre de la región: {region}: {cantidad} muertes\n\n")
        salida.write(f"\nCasos aves muertas mes enero del año 2023: {muertes_en_enero}\n")
        salida.write(f"En la comuna de Cartagena se detectaron {muertes_tagua_cartagena} Taguas muertas.\n")
        salida.write(f"Las muertes detectadas para el 12 de febrero del 2023 de la especie Piquero - (Sula variegata) son: {muertes_piquero_12f}\n")

if __name__ == "__main__":
    datos = lectura_datos("mortalidad_aves.txt") 
    muertes_region = funcion_a(datos) # respuesta al pundo a de la tarea   
    muertes_en_enero = funcion_b(datos) #respuesra al pundo b de la tarea
    muertes_tagua_cartagena = funcion_c(datos) #respuesta al punco c de la tarea
    muertes_piquero_12f = funcion_d(datos) #respuesta al punto d de la tarea
    grafico = funcion_e(datos) # respuesta al punto e de la tarea
    genera_salida(muertes_region, muertes_en_enero, muertes_tagua_cartagena, muertes_piquero_12f)