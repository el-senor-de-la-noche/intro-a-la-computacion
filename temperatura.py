def lectura():
    temperatura = float(input("indique su temperatura:"))
    edad = int(input("indique su edad: "))
    medicion_edad = bool(input("True = anios / False = meses: "))
    return [temperatura, edad, medicion_edad]
def analisis(datos):
    if datos[2] == True:
        if datos[1]>= 19:
            if datos[0] >= 36.1 and datos[0]<= 37.2:
                resultado = "normal"
            else:
                if datos[0]<36.1:
                    resultado = "baja"
                else:
                    resultado = "alta"
        else:
            if datos[1]>= 1:
                if datos[0]>= 36.5 and datos[0]<= 37.5:
                    resultado = "normal"
                else:
                    if datos[0]<36.5:
                        resultado = "baja"
                    else:
                        resultado = "alta"
            else:
                if datos[1] > 1 and datos[1]<= 5:
                    if datos[0]>= 36.5 and datos[0]<= 37.5:
                        resultado = "normal"
                    else:
                        if datos[0]<36.5:
                            resultado = "baja"
                        else:
                            resultado = "alta"
                else:
                    if datos[1] > 5 and datos[1]<=12:
                        if datos[0]>= 36.5 and datos[0]<= 37.5:
                            resultado = "normal"
                        else:
                            if datos[0]<36.5:
                                resultado = "baja"
                            else:
                                resultado = "alta"
                    else:
                        if datos[1]> 12 and datos[1]<=19:
                            if datos[0]>= 36.5 and datos[0]<= 37.5:
                                resultado = "normal"
                            else:
                                if datos[0]<36.5:
                                    resultado = "baja"
                                else:
                                    resultado = "alta"
    return resultado
def mostrar(resultado):
    print(f"su temperatura es {resultado}")

if __name__=="__main__":
    datos = lectura()
    resultado = analisis(datos)
    mostrar(resultado)
        
