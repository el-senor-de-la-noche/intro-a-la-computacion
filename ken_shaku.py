print('CONVERTIDOR DE CENTIMETROS A KENS Y SHAKUS')
cm = float(input('Escriba la cantidad de centimetros: '))
ken_cm = 6 * 30.3
ken_en_cm = cm / ken_cm
ken_int = int(ken_en_cm)
ken_shakus = ken_en_cm - ken_int
shakus = ken_shakus * 6
print(cm, 'son ', ken_int, 'ken(s) y',shakus, 'shaku(s)')