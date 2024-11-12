import os

def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def saludar():
    print('Hola a todos')

def salir():
    print('\n<<< Nos vemos >>>\n')

SEGUNDOS = 1

if __name__ == '__main__':
    print(__name__)
