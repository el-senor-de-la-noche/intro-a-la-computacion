def abrir_fichero(archivo):
    guias = []
    try:
        with open(archivo, 'r') as file:
            for line in file.readlines():
                guias.append(line.strip())  # Agregar cada línea del archivo a la lista guias
    except FileNotFoundError:
        print("El archivo no se encontró.")
    
    return guias

def buscar(guias):
    datos = []
    for guia in guias:
        # Analizar la línea para extraer el mes y el año
        # Si el mes es "julio" y el año es 2022 o 2023, agregar a datos
        pass

    return datos

def mostrar(extraccion):
    for dato in extraccion:
        print(dato)

if __name__ == "__main__":
    guias = abrir_fichero(guias.dat)
    extraccion = buscar(guias)
    mostrar(extraccion)

