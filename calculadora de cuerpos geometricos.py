
import math

print("""que cuerpo geometrico deseas calcular su area y volumen: 
      1 - Cubo
      2 - Paralelepipedo
      3 - Esfera
      4 - Cono
      5 - Piramide
      6 - Cilindro 
      """)
opcion = int(input("¿cual es la opcion que deseas?:"))
def cubo():
    a = float(input("¿cual es el valor para a?:"))
    cubo_area = 6*a**2
    cubo_volumen = a**3
    print(f"el area de el cubo es: {cubo_area}")
    print(f"el volumen de el cubo es: {cubo_volumen}")

def paralelepipedo():
    a = float(input("¿cual es el valor para a?:"))
    b = float(input("¿cual es el valor para b?:"))
    c = float(input("¿cual es el valor para c?:"))
    paralelepipedo_area = 2*(a*b+a*c+b*c)
    paralelepipedo_volumen = a*b*c
    print(f"el area del paralelepipedo es: {paralelepipedo_area}")
    print(f"el volumen del paralelepipedo es: {paralelepipedo_volumen}")

def esfera():
    a = float(input("¿cual es el valor para a?:"))
    esfera_area = 4*math.pi*(a**2)
    esfera_volumen = 4/3*math.pi*(a**3)
    print(f"el area de la esfera es: {esfera_area}")
    print(f"el volumen de la esfera es: {esfera_volumen}")

def cono():
    r = float(input("¿cual es tu radio deseado?:"))
    g = float(input("¿cual es tu valor para g?:"))
    h = float(input("¿cual es el valor que quieres para h?"))
    area_base = math.pi*(r**2)
    area_sup_curva = math.pi*r*g
    area_cono = area_base + area_sup_curva
    volumen_cono = 1 / 3*math.pi*(r**2)*h
    print(f"el area del cono es: {area_cono}")
    print(f"el volumen del cono es: {volumen_cono}")
    print(f"el area sup curva del cono es: {area_sup_curva}")
    print(f"el area base del cono es: {area_base}")
def piramide():
    a = float(input("¿cual va a ser tu a?:"))
    b = float(input("¿cual va a ser tu b?:"))
    h = float(input("¿cual va a ser tu h?:"))
    area_base2 = a*a
    area_laterales = (b*h)/2
    area_piramide = area_base2 + area_laterales
    volumen_piramide = (area_base2*h)/3
    print(f"el area de la piramide es: {area_piramide}")
    print(f"el volumen de la piramide es: {volumen_piramide}")
    print(f"el area base de la piramide es: {area_base2}")
    print(f"el area de los laterales de la piramide es: {area_laterales}")

def cilindro():
    r = float(input("¿cual es tu valor de r?:"))
    h = float(input("cual es tu valor para h?:"))
    area_cilindro = 2*math.pi*r*(r+h)
    volumen_cilindro = math.pi*r**2*h
    print(f"el area del cilindro es: {area_cilindro}")
    print(f"el volumen del cilindro es: {volumen_cilindro}")
    return

if opcion == 1:
    cubo()
elif opcion == 2:
    paralelepipedo()
elif opcion == 3:
    esfera()
elif opcion == 4:
    cono()
elif opcion == 5:
    piramide()
elif opcion == 6:
    cilindro()
else:
    opcion == 7
    print("cuerpo no encontrado")