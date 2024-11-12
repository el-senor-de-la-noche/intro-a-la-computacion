def lectura():
    glucosa = float(input("indique su nivel de Glucosa: "))
    edad = int(input("indique su edad:"))
    diferencia = bool(input("True = anios / False = meses : "))
    genero = input("0 para Masculino / 1 para Femenino: ")
    return [glucosa, edad, diferencia, genero]

def analisis(datos):
    if datos[2] == True:
        if datos[1] > 19:
            if datos[3] == "0":
                if datos[0]>= 70 and datos[0] <= 150:
                    resultado = "positivo"
                else:
                    if datos[0] < 70:
                        resultado = " hipoglucemia (bajo el rango)"
                    else:
                        resultado = "hiperglucemia (sobre el rango"
            else:
                if datos[0] >= 70 and datos[0] <= 140:
                    resultado = 'Positivo'
                else:
                    if datos[0] < 70:
                        resultado = ' hipoglucemia (bajo el rango)'
                    else:
                        resultado = 'hiperglucemia (sobre el rango)'
        else:
            if datos[1] <= 1:
                if datos[0]>= 70 and datos[0] <= 100:
                    resultado = "positivo"
                else:
                    if datos[0] < 70:
                        resultado = " hipoglucemia (bajo el rango)"
                    else:
                        resultado = "hiperglucemia (sobre el rango)"
            else:
                if datos[1] > 1 and datos[1] <= 5:
                    if datos[0] >= 80 and datos[0]<= 110:
                        resultado = "positivo"
                    else:
                        if datos[0] < 80:
                            resultado = " hipoglucemia (bajo el rango)"
                        else:
                            resultado = "hiperglucemia (sobre el rango"
                else:
                    if datos[1] > 5 and datos[1] <=12:
                        if datos[0] >= 70 and datos[0] <= 130:
                            resultado = "positivo"
                        else:
                            if datos[0]<70:
                                resultado = " hipoglucemia (bajo el rango)"
                            else:
                                resultado = "hiperglucemia (sobre el rango"
                    else:
                        if datos[1]>12 and datos[1]<=19:
                            if datos[0] >=70 and datos[0] <= 120:
                                resultado = "positivo"
                            else:
                                if datos[0] > 70:
                                    resultado = " hipoglucemia (bajo el rango)"
                                else:
                                    resultado = "hiperglucemia (sobre el rango)"
                                


    return resultado
def muestra_resultado(resultado):
    print (f" tu resultadi es: {resultado}")

if __name__ == '__main__':
    datos = lectura()
    resultado = analisis(datos)
    muestra_resultado(resultado)