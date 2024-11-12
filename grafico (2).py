#Author
#Luis Ponce y NNNNN

import matplotlib.pyplot as plt


def definir_datos_y(y1, y2, y3, y4, y5):
    # datos
    datos = [y1, y2, y3, y4, y5]
    return datos


def define_etiquetas_x(a, b, c, d, e):
    # Definir las etiquetas para cada barra
    etiquetas = [a, b, c, d, e]
    return etiquetas


def crear_grafico(etiquetas, datos):
    # Crear el gráfico de barras
    plt.bar(etiquetas, datos)
    # Agregar título y etiquetas al eje X e Y
    plt.title("Gráfico de Ejemplo")
    plt.xlabel("Meses en eje X")
    plt.ylabel("Valores eje Y")
    # Mostrar el gráfico
    plt.show()


# Código que solo se ejecuta cuando se ejecuta el script directamente
if __name__ == "__main__":
    datos_y = definir_datos_y(5, 3, 8, 12, 10)
    etiquetas_x = define_etiquetas_x("Enero", "Febrero", "Marzo", "Abril", "mayo")
    crear_grafico(etiquetas_x, datos_y)
