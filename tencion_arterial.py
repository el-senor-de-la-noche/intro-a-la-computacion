def lectura():
    nivel_hierro = float(input("indique su nivel de hierro: "))
    edad = int(input("indique su edad: "))
    medicion_edad = bool(input("True = anios / False = meses: "))
    genero = input("0 = masculino / 1 = femenino: ")
    return[nivel_hierro, edad, medicion_edad, genero]
def analisis(datos):
    if datos[2] == True:
        if datos[1]<= 19:
            if datos[3] == "0":
                if datos[0]>= 70 and datos[0]<= 160:
                    resultado = "normal"
                else:
                    if datos[0]<70:
                        resultado = "deficiencia de hierro"
                    else:
                        resultado = "sobrecarga de hierro"
            else:
                if datos[0]>=60 and datos[0]<= 140:
                    resultado = "normal"
                else:
                    if datos[0]<60:
                        resultado = "deficiencia de hierro"
                    else:
                        resultado = "sobrecarga de hierro"
        else:
            if datos[1]<=1:
                if datos[0] >= 50 and datos[0]<=120:
                    resultado = "normal"
                else:
                    if datos[0]<50:
                        resultado = "deficiencia de hierro"
                    else:
                        resultado = "sobrecarga de hierro"
            else:
                if datos[1] > 1 and datos[1]<= 5:
                    if datos[0]>= 60 and datos[0]<= 130:
                        resultado = "normal"
                    else:
                        if datos[0]<60:
                            resultado = "deficiencia de hierro"
                        else:
                            resultado = "sobrecarga de hierro"
                else:
                    if datos[1] >5 and datos[1]<= 12:
                        if datos[0]>=70 and datos[0]<= 140:
                            resultado = "normal"
                        else:
                            if datos[0]<70:
                                resultado = "deficiencia de hierro"
                            else:
                                resultado = "sobrecarga de hierro"
                    else:
                        if datos[1] > 12 and datos[1] <= 19:
                            if datos[0]>= 80 and datos[0]<= 150:
                                resultado = "normal"
                            else:
                                if datos[0]<80:
                                    resultado = "deficiencia de hierro"
                                else:
                                    resultado = "sobrecarga de hierro"
    return resultado
def mostrar(resultado):
    print(resultado)

if __name__ == "__main__":
    datos = lectura()
    resultado = analisis(datos)
    mostrar(resultado)