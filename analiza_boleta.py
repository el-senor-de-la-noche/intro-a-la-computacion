#Integrante 1: Steven Cifuentes Luengo
#Integrante 2: Matías Rodrígez Hernandez

def lectura_archivo(nombre):
    #Esta función busca leer un archivo de boletas y devolver los datos solicitados de manera ordenada.
    ar = open(nombre, 'r')
    datos = []
    #Lee cada linea del archivo, los procesa y añade a la lista 'datos'.
    for archivos in ar:
      var = archivos.strip('\n').split(',')
      boleta = []
      #La única información que nos interesa es el folio, la fecha y el valor neto de la boleta.
      boleta.append(var[1]), boleta.append(var[2]), boleta.append(var[10])
      datos.append(boleta)
    ar.close()
    return datos


def meses(datos):
  #Con los datos leidos, tenemos la información de más de cien mil boletas. Queremos saber cuánto se vendió en cada mes.
  #Dividimos las ventas totales del año en sus respectivos meses según su número.
  dicc_2021 = {'02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0
                 , '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}
  dicc_2022 = {'01': 0, '02': 0, '03': 0, '04':0, '05': 0, '06': 0
                 , '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}
  dicc_2023 = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0
                 , '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}
  for boleta in datos:
    aux = boleta[1].split('-')
    #Sumamos la venta de cada boleta al mes de su emisión.
    if aux[0] == '2021':
      dicc_2021[aux[1]] += float(boleta[2])
    elif aux[0] == '2022':
      dicc_2022[aux[1]] += float(boleta[2])
    elif aux[0] == '2023':
      dicc_2023[aux[1]] += float(boleta[2])
  #La función devuelve una lista con el el valor de las ventas totales de cada mes.
  diccionarios = []
  diccionarios.append(dicc_2021)
  diccionarios.append(dicc_2022)
  diccionarios.append(dicc_2023)
  return diccionarios


def venta_mayor(datos):
  #Esta función busca y devuelve el mes con la mayor cantidad de ventas para cada año basándose en los datos proporcionados.  
  diccionarios = meses(datos) 
  mayor_lista = []
  mesi = {'01': 'Enero', '02': 'Febrero', '03': 'Marzo',
           '04': 'Abril', '05': 'Mayo', '06': 'Junio', '07': 'Julio',
            '08': 'Agosto', '09': 'Septiembre', '10': 'Octubre',
              '11': 'Noviembre', '12': 'Diciembre'} #Mesi significa meses en italiano
  for anio in diccionarios: 
    #Este algoritmo busca el mes con las mayores ventas por año, comparando las ventas de cada mes para encontrar el mes con la mayor cantidad de ventas en cada año.
    aux = 0  
    boleta_actual = []
    for mes in anio:
      if float(anio[mes]) > aux:
        aux = float(anio[mes]) 
        boleta_actual = [mesi[mes], anio[mes]]
    mayor_lista.append(boleta_actual)
  print(mayor_lista)
  return mayor_lista


def venta_menor(datos):
  #Esta función busca y devuelve el mes con la menor cantidad de ventas para cada año basándose en los datos proporcionados.  
  diccionarios = meses(datos)
  menor_lista = []
  mesi = {'01': 'Enero', '02': 'Febrero', '03': 'Marzo',
           '04': 'Abril', '05': 'Mayo', '06': 'Junio', '07': 'Julio',
            '08': 'Agosto', '09': 'Septiembre', '10': 'Octubre',
              '11': 'Noviembre', '12': 'Diciembre'}
  for anio in diccionarios:
    #El mismo algortimo de la funcion venta_mayor(), solo que lo usamos al revés. 
    #Comparamos las ventas de cada para encontrar la menor cantidad de ventas en cada año.
    aux = 9999999999
    boleta_actual = []
    for mes in anio:
      if float(anio[mes]) < aux:
        aux = float(anio[mes])
        boleta_actual = [mesi[mes], anio[mes]]
    menor_lista.append(boleta_actual) 
  return menor_lista


def encontrar_restante(folios):
  #Esta función busca los folios faltantes en cada año.
  restante = [[], [], []]
  for i in range(1, 110785):
    #Vamos número a número buscando si falta un folio. Si falta, agrega el número faltante a la lista 'restantes' en su respectivo orden.
    if str(i) not in folios:
      if i >= 1 and i < 23681:
        restante[0].append(str(i))
      elif i >= 23681 and i < 78222:
        restante[1].append(str(i))
      elif i >= 78222 and i < 110785:
        restante[2].append(str(i))
    else:
      del folios[folios.index(str(i))]
  #La función devuelve una lista vacia en caso de que todos los folios se encuentre.
  #En caso contrario, devuelve una lista con los números faltantes
  return restante


def revision_correlativo(datos):
  #Esta función crea una lista de todos los números de folios para luego enviar esta lista a una revisión
  folios = []
  for boleta in datos:
    folios.append(boleta[0])
  correlativo = encontrar_restante(folios)
  return correlativo


def genera_informe(mayor_lista, menor_lista, correlativo):
  #Esta función crea un archivo donde podemos ver todos los datos obtenidos de manera ordenada.
  ar = open('infoboletas.txt', 'w')
  ar.write('Reporte de analisis automatico.' + '\n')  
  ar.write('Fecha de reporte: ' + '17/12/2023' + '\n')
  ar.write('Ventas Menor 2021' + '\n')
  ar.write(menor_lista[0][0] + ' : ' + str(menor_lista[0][1]) + '\n') 
  ar.write('Ventas Mayor 2021' + '\n')
  ar.write(mayor_lista[0][0] + ' : ' + str(mayor_lista[0][1]) + '\n') 
  ar.write('Folios de boletas correlativos faltantes' + '\n')
  if correlativo[0] == []:
    ar.write('\n')
  else:
    for valor in correlativo[0][:-1]:
      ar.write(valor + ' - ')
    ar.write(correlativo[0][-1] + '\n') 
  ar.write('Fin 2021' + '\n') 

  ar.write('Ventas Menor 2022' + '\n')
  ar.write(menor_lista[1][0] + ' : ' + str(menor_lista[1][1]) + '\n') 
  ar.write('Ventas Mayor 2022' + '\n')
  ar.write(mayor_lista[1][0] + ' : ' + str(mayor_lista[1][1]) + '\n')
  ar.write('Folios de boletas correlativos faltantes' + '\n')
  if correlativo[1] == []:
    ar.write('\n')
  else:
    for valor in correlativo[1][:-1]:
      ar.write(valor + ' - ')
    ar.write(correlativo[1][-1] + '\n')
  ar.write('Fin 2022' + '\n') 
  ar.write('Ventas Menor 2023' + '\n')
  ar.write(menor_lista[2][0] + ' : ' + str(menor_lista[2][1]) + '\n')
  ar.write('Ventas Mayor 2023' + '\n')
  ar.write(mayor_lista[2][0] + ' : ' + str(mayor_lista[2][1]) + '\n')
  ar.write('Folios de boletas correlativos faltantes' + '\n') 
  if correlativo[2] == []:
    ar.write('\n')
  else:
    for valor in correlativo[2][:-1]:
      ar.write(valor + ' - ')
    ar.write(correlativo[2][-1] + '\n') 
  ar.write('Fin 2023' + '\n')
  ar.write('Fin Transaccion') 

if __name__ == '__main__':
 #Función principal
 datos = lectura_archivo('boletas.txt')
 mayor_lista = venta_mayor(datos)
 menor_lista = venta_menor(datos)
 correlativo = revision_correlativo(datos)
 genera_informe(mayor_lista, menor_lista, correlativo)
