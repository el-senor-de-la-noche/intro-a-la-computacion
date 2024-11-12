def lectura():
    hemo = float(input("Nivel de hemoglobina: "))
    edad = int(input('Ingrese edad: '))
    tipo = bool(input('True = Meses / False = Agnos: '))
    genero = input('0 para Masculino / 1 para Femenino: ')
    return [hemo, edad, tipo, genero]

def analisis(datos):
    if datos[1] > 15:
        if datos[3] == '0':
            if datos[0] >= 14 and datos[0] <= 18:
                resultado = 'Positivo'
            else:
                if datos[0] < 14:
                    resultado = 'Negativo (Bajo Rango)'
                else:
                    resultado = 'Negativo (Sobre Rango)'
        else:
            if datos[0] >= 12 and datos[0] <= 16:
                resultado = 'Positivo'
            else:
                if datos[0] < 12:
                    resultado = 'Negativo (Bajo Rango)'
                else:
                    resultado = 'Negativo (Sobre Rango)'
    else:
        if datos[2] == True:
            if datos[1] <= 1:
                if datos[0] >= 13 and datos[0] <= 26:
                    resultado = 'Positivo'
                else:
                    if datos[0] < 13:
                        resultado = 'Negativo (Bajo Rango)'
                    else:
                        resultado = 'Negativo (Sobre Rango)'
            else:
                if datos[1] > 1 and datos[1] <= 6:
                    if datos[0] >= 10 and datos[0] <= 18:
                        resultado = 'Positivo'
                    else:
                        if datos[0] < 10:
                            resultado = 'Negativo (Bajo Rango)'
                        else:
                            resultado = 'Negativo (Sobre Rango)'
                else:
                    if datos[1] > 6 and datos[1] <= 12:
                        if datos[0] >= 11 and datos[0] <= 15:
                            resultado = 'Positivo'
                        else:
                            if datos[0] < 11:
                                resultado = 'Negativo (Bajo Rango)'
                            else:
                                resultado = 'Negativo (Sobre Rango)'
        else:
            if datos[1] > 1 and datos[1] <= 5:
                if datos[0] >= 11.5 and datos[0] <= 15:
                    resultado = 'Positivo'
                else:
                    if datos[0] < 11.5:
                        resultado = 'Negativo (Bajo Rango)'
                    else:
                        resultado = 'Negativo (Sobre Rango)'
            else:
                if datos[1] > 5 and datos[1] <= 10:
                    if datos[0] >= 12.6 and datos[0] <= 15.5:
                        resultado = 'Positivo'
                    else:
                        if datos[0] < 12.6:
                            resultado = 'Negativo (Bajo Rango)'
                        else:
                            resultado = 'Negativo (Sobre Rango)'
                else:
                    if datos[1] > 10 and datos[1] <= 15:
                        if datos[0] >= 13 and datos[0] <= 15.5:
                            resultado = 'Positivo'
                        else:
                            if datos[0] < 13:
                                resultado = 'Negativo (Bajo Rango)'
                            else:
                                resultado = 'Negativo (Sobre Rango)'      
    return resultado

def muestra_resultado(resultado):
    print (resultado)

if __name__ == '__main__':
    datos = lectura()
    resultado = analisis(datos)
    muestra_resultado(resultado)