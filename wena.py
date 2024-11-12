#autor: Gabriel Alonso Paredes Fuentes y Daniel Navarrete Silva
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
    regiones = []
    muertes_por_region = []
    for muerte in datos:
        region = muerte[2]
        cantidad_muertes = muerte[7]
        if region in muertes_por_region:
            muertes_por_region[region] = region + cantidad_muertes
    return muertes_por_region
def funcion_b(datos):
    cantidad = 0
    for muerte in datos:
        if muerte[0] == "2023-01":
            cantidad = cantidad + muerte[7]
    return cantidad
def funcion_c(datos):
    cantidad = 0
    for muerte in datos:
        if muerte[6].lower() == " Tagua - (Columba fasciata)" and muerte[3] == "Cartagena":
            cantidad = cantidad + muerte[7]

    return cantidad
def funcion_d(datos):
    cantidad = 0  
    for muerte in datos:
        if muerte[0] == "2023-02-12" and muerte[6] == "Piquero - (Sula variegata)":
            cantidad = cantidad + muerte[7]
    return cantidad
def funcion_e(datos):
    especies =["Gaviota garuma - (Larus modestus)", "Piquero - (Sula variegata)", "Gaviota de Franklin - (Larus pipixcan)", "Pelicano - (Pelecanus thagus)", "Guanay - (Phalacrocorax bougainvillii)"]
    conteo_especies = 0
    for especie in datos:
        if especie[6]== especies[0]:
            index = conteo_especies[especies]
            conteo_especies[index] = conteo_especies[index] + especie[7]
        

    plt.figure(figsize=(10, 5))
    plt.bar(especies, conteo_especies)
    plt.xlabel('Especies')
    plt.ylabel('Cantidad de muertes')
    plt.title('Cantidad de muertes por especie')
    plt.show()

def genera_salida( muertes_region, muertes_en_enero, muertes_tagua_cartagena, muertes_piquero_12f):
    pass
if __name__ == "__main__":
    datos = lectura_datos("mortalidad_aves.txt")
    muertes_region = funcion_a(datos)
    muertes_en_enero = funcion_b(datos)
    muertes_tagua_cartagena = funcion_c(datos)
    print(muertes_tagua_cartagena)
    muertes_piquero_12f = funcion_d(datos)    
    funcion_e(datos)
    genera_salida( muertes_region, muertes_en_enero, muertes_tagua_cartagena, muertes_piquero_12f)
