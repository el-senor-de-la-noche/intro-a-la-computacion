def lectura():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    grasa_corporal = float(input("Porcentaje de grasa corporal (%): "))
    vo2_max = float(input("VO2 Máximo (mL/kg/min): "))
    edad = int(input('Ingrese edad: '))
    genero = input('0 para Masculino / 1 para Femenino: ')
    return [peso, altura, grasa_corporal, vo2_max, edad, genero]

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def analisis(datos):
    peso, altura, grasa_corporal, vo2_max, edad, genero = datos
    imc = calcular_imc(peso, altura)
    
    if imc <= 24.0:
        if grasa_corporal < 15 and vo2_max > 55:
            resultado = 'Excelente'
        elif 15 <= grasa_corporal <= 20 and 45 <= vo2_max <= 55:
            resultado = 'Buena'
        elif 20 < grasa_corporal <= 25 and 35 <= vo2_max <= 44:
            resultado = 'Regular'
        else:
            resultado = 'Mala'
    elif 24.1 <= imc <= 29.0:
        if 20 <= grasa_corporal <= 25 and 35 <= vo2_max <= 44:
            resultado = 'Regular'
        else:
            resultado = 'Mala'
    else:
        resultado = 'Mala'

    return resultado

def muestra_resultado(resultado):
    print(f"Categoría de condición física: {resultado}")

if __name__ == '__main__':
    datos = lectura()
    resultado = analisis(datos)
    muestra_resultado(resultado)
