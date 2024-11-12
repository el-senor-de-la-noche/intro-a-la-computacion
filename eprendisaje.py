def lectura():
    glucosa = float(input("ingrese su nivel de glucosa: "))
    edad = int(input("ingrese su edad"))
    medicion = bool(input("True = anios / False = meses "))
    genero = input("0 = hombre  / 1 = mujer")
    return [glucosa, edad, medicion, genero]
def analisis(datos):
    if datos[3]== "0":
        if datos[1]> 19:
            if datos[0] >= 70 and datos[0]<= 150:
                resultado = "normal"
            else:
                if datos[0]<70:
                    resultado = "hipoglucemia (bajo el rango)"
                else:
                    resultado = "hiperglucemia (sobre el rango)"
    else:
        if datos            
def mostrar(resultado):
    pass

if __name__ == "__main__":
    datos = lectura()
    resultado = analisis(datos)
    mostrar(resultado)