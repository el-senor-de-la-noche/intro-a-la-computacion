def abrir_fichero(nombre_matriz):
    try:
        archivo = open(nombre_matriz, 'r')
        
        A = []
        B = []
        
        # Leer la matriz A
        for i in range(2):
            linea = archivo.readline().strip()
            fila = list(map(int, linea.split()))
            if len(fila) != 2:
                raise ValueError("Cada línea debe contener exactamente dos números enteros.")
            A.append(fila)
        
        # Leer la matriz B
        for i in range(2):
            linea = archivo.readline().strip()
            fila = list(map(int, linea.split()))
            if len(fila) != 2:
                raise ValueError("Cada línea debe contener exactamente dos números enteros.")
            B.append(fila)
        
        archivo.close()
        
        return A, B
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_matriz}' no fue encontrado.")
        exit(1)
    except ValueError as e:
        print(f"Error de formato en el archivo: {e}")
        exit(1)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        exit(1)

def sumar_matriz(A, B):
    C = [[0, 0], [0, 0]]
    
    # Sumar las matrices A y B
    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] + B[i][j]
    
    return C

def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

def main():
    nombre_matriz = "matriz.txt"
    A, B = abrir_fichero(nombre_matriz)
    C = sumar_matriz(A, B)
    mostrar_matriz(C)

if __name__ == "__main__":
    main()
