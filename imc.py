def lectura():
    imc = float(input("indique el imc del paciente: "))
    edad = int(input("indique la edad del paciente: "))
    diferencia = bool(input("True = anios / False = meses: "))
    genero = input("0 para hombre / 1 para mujer:  ")
    return [imc, edad, diferencia, genero]
def analisis(datos):
    if datos[2] == True:
        if datos[1]> 19:
            if datos[3] == "0":
                if datos[0]>= 18.5 and datos[0] <= 24.9:
                    resultado = "peso normal"
                else:
                    if datos[0]<18.5:
                        resultado = "esta bajo peso"
                    else:
                        if datos[0] >= 25 and datos[0]<=29:
                            resultado = "tiene sobrepeso"
                        else:
                            resultado = "tiene obesidad"
            else:
                if datos[0]>= 18.5 and datos[0] <= 24.9:
                    resultado = "peso normal"
                else:
                    if datos[0]<18.5:
                        resultado = "esta bajo peso"
                    else:
                        if datos[0] >= 25 and datos[0]<=29:
                            resultado = "tiene sobre peso"
                        else:
                            resultado = "tiene obesidad"
        else:
            if datos[1]<=1:
                if datos[0]>=14.5 and datos[0]<=18:
                    resultado = "peso normal"
                else:
                    if datos[0] < 14.5:
                        resultado = "esta bajo peso"
                    else:
                        if datos[0]>= 18.1 and datos[0]<=20:
                            resultado = "tiene sobre peso"
                        else:
                            resultado = "tiene obesidad"
            else:
                if datos[1]>=1 and datos[1] <= 5:
                    if datos[0]>=14 and datos[0]<=18.5:
                       resultado = "peso normal"
                    else:
                        if datos[0]<14:
                            resultado= "esta bajo peso"
                        else:
                            if datos[0]>=18.6 and datos[0]<= 21:
                                resultado = "esta sobrepeso"
                            else:
                                resultado = "tiene obesidad"
                else:
                    if datos[1]>=12 and datos[1]<=19:
                        if datos[0]>=15 and datos[0]<=22:
                            resultado = "peso normal"
                        else:
                            if datos[0]<15:
                                resultado = "esta bajo peso"
                            else:
                                if datos[0]>=22.1 and datos[0]<=25:
                                    resultado= "tiene sobrepeso"
                                else:
                                    resultado = "tiene obesidad"
    return resultado
def mostrar_resultado(resultado):
    print(resultado)


if __name__ == '__main__':
    datos = lectura()
    resultado = analisis(datos)
    mostrar_resultado(resultado)