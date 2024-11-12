frase = 'La reina que calzaba unas zapatillas este lunes llego al Teatro Real en Madrid para asistir a un concierto organizado por la Fundacion Princesa de Girona y fue vista cojear debido a la molestia que le causa la lesion'
palabras = frase.lower().split(' ')
palabra = input('Palabra a buscar: ').lower()
# i = 0
# contador = 0
# while i < len(palabras):
#     if palabra == palabras[i]:
#         contador = contador + 1
#     i = i + 1

# Version 2

contador = palabras.count(palabra)
print('Repetidas: ', contador)

