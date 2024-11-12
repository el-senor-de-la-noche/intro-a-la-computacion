import os
def limpirar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def lectura():
    frecuencia_cardiaca = float(input("indique su frecuencia cardiaca: "))
    edad = int(input("indiuque su edad: "))
    medicion_edad= bool(input("True = anios / False = meses: "))
    genero = input("0 = masculino / 1 = femenino: ")
    return [frecuencia_cardiaca, edad, medicion_edad, genero]
def analisis(datos):
    if datos[2] == True:
        if datos[1] > 19:
            if datos[3] == "0":
                if datos[0]>=60 and datos[0]<= 100:
                    resultado = "normal"
                else:
                    if datos[0] < 60:
                        resultado = "baja (bradicardia)"
                    else:
                        resultado = "alta (taquicardia)"
            else:
                if datos[0]>=60 and datos[0]<= 100:
                    resultado = "normal"
                else:
                    if datos[0] < 60:
                        resultado = "baja (bradicardia)"
                    else:
                        resultado = "alta (taquicardia)"
        else:
            if datos[1]<=1:
                if datos[0]>=100 and datos[0]<= 160:
                    resultado = "normal"
                else:
                    if datos[0] < 100:
                        resultado = "baja (bradicardia)"
                    else:
                        resultado = "alta (taquicardia)"
            else:
                if datos[1] > 1 and datos[1] <=5:
                    if datos[0]>=80 and datos[0]<= 130:
                        resultado = "normal"
                    else:
                        if datos[0] < 80:
                            resultado = "baja (bradicardia)"
                        else:
                            resultado = "alta (taquicardia)"
                else:
                    if datos[1]>5 and datos[1]<=12:
                        if datos[0]>=70 and datos[0]<= 120:
                            resultado = "normal"
                        else:
                            if datos[0] < 70:
                                resultado = "baja (bradicardia)"
                            else:
                                resultado = "alta (taquicardia)"
                    else:
                        if datos[1]>12 and datos[1]<= 19:
                            if datos[0]>=60 and datos[0]<= 100:
                                resultado = "normal"
                            else:
                                if datos[0] < 60:
                                    resultado = "baja (bradicardia)"
                                else:
                                    resultado = "alta (taquicardia)"
    return resultado
def mostrar(resultado):
    print(f" resultado es {resultado}" )

if __name__ == "__main__":
    limpirar()
    datos = lectura()
    resultado = analisis(datos)
    mostrar(resultado)

