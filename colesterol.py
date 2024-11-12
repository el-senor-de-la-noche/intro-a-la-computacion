def lectura():
    colesterol = float(input("indique el colesterol del paciente: " ))
    edad = int(input("indique la edad: "))
    diferencia = bool(input("True = anios / False = meses: "))
    genero = input("0 para hombre / 1 para mujer:  ")
    return [colesterol, edad, diferencia, genero]
def analisis(datos):
    if datos[2]== True:
        if datos[1]>19:
            if datos[3] == "0":
                if datos[0]>=170 and datos[0]<=210:
                    resultado = "normal"
                else:
                    if datos[0]< 170:
                        resultado = " hipocolesterolemia (bajo el rango)"
                    else:
                        resultado = "hipercolesterolemia (sobre el rango)"
            else:
                if datos[0]>=160 and datos[0]<=200:
                    resultado = "normal"
                else:
                    if datos[0]<160:
                        resultado = " hipocolesterolemia (bajo el rango)"
                    else:
                       resultado = "hipercolesterolemia (sobre el rango)"
        else:
            if datos[1]<=1:
                if datos[0]>= 120 and datos[0]<=160:
                    resultado = "normal"
                else:
                    if datos[0]<120:
                        resultado = "hipocolesterolemia (bajo el rango)"
                    else:
                        resultado = "hipercolesterolemia (sobre el rango)"
            else:
                if datos[1]>=1 and datos[1]<= 5:
                    if datos[0]>=130 and datos[0]<=170:
                        resultado = "normal"
                    else:
                        if datos[0]<130:
                            resultado = "hipocolesterolemia (bajo el rango)"
                        else:
                             resultado = "hipercolesterolemia (sobre el rango)"
                else:
                    if datos[1]>=5 and datos[1]<= 12:
                        if datos[0]>= 140 and datos[0]<= 180:
                            resultado = "normal"
                        else:
                            if datos[0]<140:
                                resultado = "hipocolesterolemia (bajo el rango)"
                            else:
                                resultado = "hipercolesterolemia (sobre el rango)"
                    else:
                        if datos[1]>=12 and datos[1]<=19:
                            if datos[0]>=150 and datos[0]<=190:
                                resultado =  "normal"
                            else:
                                if datos[0]<150:
                                    resultado = "hipocolesterolemia (bajo el rango)"
                                else:
                                    resultado = "hipercolesterolemia (sobre el rango)"
        return resultado
def mostrar(resultado):
    print(resultado)

if __name__ == "__main__":
    datos = lectura()
    resultado = analisis(datos)
    mostrar(resultado)