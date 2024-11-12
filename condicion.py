def lectura():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    grasa_corporal = float(input("Porcentaje de grasa corporal (%): "))
    vo2_max = float(input("VO2 Máximo (mL/kg/min): "))
    edad = int(input('Ingrese edad: '))
    genero = input('0 para Masculino / 1 para Femenino: ')
    return [peso, altura, grasa_corporal, vo2_max, edad, genero]
def imc(datos):
    peso = float(datos[0])
    altura = float(datos[1])
    imc = peso / (altura**2)
    return imc
def analisis(datos, imc):
    if imc <= 24.0:
        if datos[2]<15 and datos[3] >55:
            resultado = "exelente"
        else:
            if datos[2] >= 15 and datos[2]<= 20:
                if datos[3]>= 45 and datos[3] <= 55:
                    resultado = "buena"
            else:
                if datos[2] > 20 and datos[2]<= 25:
                    if datos[3]>= 35 and datos[3]<= 44:
                        resultado = "regular"
                    else:
                        resultado = "mala"
    else:
        if imc >=24.1 and imc <= 29.0:
            if datos[2] >= 20 and datos[2] <=25:
                if datos[3]>= 35 and datos[3]<=44:
                    resultado = "regular"
            else:
                resultado = "mala"
        else:
            resultado = "mala"    
    return resultado
def muestra(resultado):
    print(f"categoria de condicion fisica :{resultado}")
if __name__ == "__main__":
    datos = lectura()
    imc = imc(datos)
    resultado = analisis(datos, imc)
    muestra(resultado)