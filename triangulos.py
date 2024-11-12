import os
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")



x = int(input("ingresa un numero: "))
if x <= 10:
    print("hola carlita")
elif x >= 10:
    print("wena wena")