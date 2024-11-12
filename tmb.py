import os
def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def lectura():
    frecuencia = float(input("indique su frecuencia cardiaca en reposo: "))
    edad = int(input("indique su edad: "))
    diferencia = bool(input("True = meses / False = anios: "))
    genero = input("0 = masculino / 1 = femenino: ")
    return [frecuencia, edad, diferencia, genero]

def analisis(datos):
    if datos[1]>=19:
        if datos[3] == "0":
            if datos[0] >= 60 and datos[0]<= 80:
                resultado = "normal"
            else:
                if datos[0] < 60:
                    resultado = "bradicardia (frecuencia cardíaca baja)"
                else:
                    resultado = "taquicardia (frecuencia cardíaca alta)"
        else:
            if datos[0]>= 60 and datos[0]<= 90:
                resultado = "normal"
            else:
                if datos[0]< 60:
                    resultado = "bradicardia (frecuencia cardíaca baja)"
                else:
                    resultado = "taquicardia (frecuencia cardíaca alta)"
    else:
        if datos[2] == True:
            if datos[1]<= 1:
                if datos[0]>=100 and datos[0]<=160:
                    resultado = "normal"
                else:
                    if datos[0]<100:
                        resultado = "bradicardia (frecuencia cardíaca baja)"
                    else:
                        resultado = "taquicardia (frecuencia cardíaca alta)"
        else:
            if datos[1]>1 and datos[1]<= 10:
                if datos[0]>= 70 and datos[0]<= 130:
                    resultado = "normal"
                else:
                    if datos[0]<70:
                        resultado = "bradicardia (frecuencia cardíaca baja)"
                    else:
                        resultado = "taquicardia (frecuencia cardíaca alta)"
            else:
                if datos[1]>10 and datos[1]<= 19:
                    if datos[0]>= 60 and datos[0] <= 100:
                        resultado = "normal"
                    else:
                        if datos[0]< 60:
                            resultado = "bradicardia (frecuencia cardíaca baja)"
                        else:
                            resultado = "taquicardia (frecuencia cardíaca alta)"
    return resultado
                            
    

def mostrar(resultado):
    print(f"tu resultado es : {resultado}")



if __name__ == '__main__':
    limpiar()
    datos = lectura()
    resultado = analisis(datos)
    mostrar(resultado)