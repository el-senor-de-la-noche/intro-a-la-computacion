letras = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lista = []
i = 0
while i < len(letras):
    if letras[i] != ' ':
        lista.append(letras[i])
    i = i + 1
print (lista)
lista1 = letras.split()
print(lista1)

