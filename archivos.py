def open(matriz):
    with open(matriz, 'r') as archivo:
        lineas = archivo.readlines()

    matriz_a = []
    matriz_b = []

    for i in range(2):
        fila = list(map(int, lineas[i].strip().split()))
        matriz_a.append(fila)

    for i in range(2, 4):
        fila = list(map(int, lineas[i].strip().split()))
        matriz_b.append(fila)

    return matriz_a, matriz_b

def sumar_matriz(A, B):
    C = []
    for i in range(2):
        fila = []
        for j in range(2):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

def main():
    nombre_matriz = 'matriz.dat'
    A, B = open(nombre_matriz)
    C = sumar_matriz(A, B)
    print("Matriz A:")
    mostrar_matriz(A)
    print("\nMatriz B:")
    mostrar_matriz(B)
    print("\nMatriz C (A + B):")
    mostrar_matriz(C)

if __name__ == "__main__":
    main()
