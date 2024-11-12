import tkinter as tk
from tkinter import ttk
def funcion_click():
    accion.configuire(text="** Has hecho click!**")
    etiqueta.configure(foreground = "red")
if __name__=="__main__":
    ventana = tk.Tk()
    ventana.title("Python - Tkinter")
    etiqueta = ttk.Label(ventana, text="hola carlita")
    ventana.resizable(0,0)
    etiqueta.grid(column=0, row=0)
    accion = ttk.Button(ventana, text ="click", command= funcion_click)
    accion.grid(column = 1, row = 0)
ventana.mainloop()