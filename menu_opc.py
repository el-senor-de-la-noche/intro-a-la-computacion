import mibib as yo
import time

def dibujar_menu():
    yo.limpiar()
    print('Selector de opciones.')
    print('---------------------')
    print('\t1 : Opcion 1')
    print('\t2 : Opcion 2')
    print('\t3 : Opcion 3')
    print('\t4 : Opcion 4')
    print('\n\tS : Salir')

def dibujar_menu1(cantidad):
    yo.limpiar()
    print('Selector de opciones.')
    print('---------------------')
    i = 1
    while i <= cantidad:
        print(str(i)+': Opcion '+ str(i))
        i +=1
    print('S : Salir')

def opcion1(mensaje, numero):
    i = 0
    while i < numero:
        print(mensaje)
        i += 1
    time.sleep(yo.SEGUNDOS)

def opcion2():
    print('Opcion 2....')
    time.sleep(yo.SEGUNDOS)

def opcion3():
    print('Opcion 3....')
    time.sleep(yo.SEGUNDOS)

def opcion4():
    print('Opcion 4....')
    time.sleep(yo.SEGUNDOS)

def menu():
    dibujar_menu()
    opcion = input('Opcion: ')
    while opcion.upper() != 'S':
        if opcion == '1':
            opcion1('Estoy en la funcion 1', 3)
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            opcion4()
        else:
            print('Opcion no valida. Reintente')
            seguir = input('Presiona <enter> para continuar')
        yo.limpiar()
        dibujar_menu()
        opcion = input('Opcion: ')

if __name__ == '__main__':
    yo.limpiar()
    menu()
    yo.salir()
