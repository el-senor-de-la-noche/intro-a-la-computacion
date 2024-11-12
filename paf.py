import os

def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def lectura():
    x1 = float(input("indique su primer punto x: "))
    y1 = float(input("indique su primer punto y: "))
    z1 = float(input("indique su primer punto z: "))
    x2 = float(input("indique su segundo punto x: "))
    y2 = float(input("indique su segundo punto y: "))
    z2 = float(input("indique su segundo punto z: "))
    return[x1,y1,z1,x2,y2,z2]
def diferencia(datos):
    diferencia = [(datos[0]-datos[3]),(datos[1]-datos[4]), (datos[2]-datos[5])]
    return diferencia
def vectores(datos):
    vectores = [(datos[5]-datos[0]), (datos[1], datos[2])(datos[3],datos[4], datos[5])]
    return vectores
def mostrar(datos, diferencia, vectores):
    print("resultados:")
    print(f"primeros punto: {datos[0],datos[1], datos[2]}")
    print(f"segundo punto: {datos[3], datos[4], datos[5]}")
    print(f"difecencia: {diferencia}")
    print(f"vectores: {vectores}")
if __name__=="__main__":
    limpiar()
    datos = lectura()
    diferencia = diferencia(datos)
    vectores = vectores(datos)
    mostrar(datos,diferencia, vectores)