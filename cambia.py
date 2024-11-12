
def lee_raw(nombre):
    ent = open(nombre)
    crudo = []
    for linea in ent:
        linea = linea.rstrip('\n')
        crudo.append(linea)
    ent.close()
    return crudo

def cambia(crudo):
    datos = []
    for linea in crudo:
        salida = ''
        i = 0
        while i < len(linea):
            caracter = linea[i]
            if caracter == '"':
                salida = salida + caracter
                i = i + 1
                caracter = linea[i]
                while caracter != '"':
                    if caracter == ',':
                        caracter = ';'
                    salida = salida + caracter
                    i = i + 1
                    caracter = linea[i]
            salida = salida + caracter
            i = i + 1
        datos.append(salida)
    return datos

def nuevo_archivo(datos):
    sal = open('mortalidad.txt', 'w')
    for dato in datos:
        sal.write(dato+'\n')
    sal.close()

if __name__ == "__main__":
    crudo = lee_raw('mortalidad_aves.txt')
    datos = cambia(crudo)
    nuevo_archivo(datos)