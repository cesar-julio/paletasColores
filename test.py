from tkinter import *
from tkinter import ttk

import tkinter as tk


class aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Pale color")
        self.raiz.resizable(width=False, height=False)
        self.raiz.config(bg="DIMGRAY")

        # ===== componetes graficos =====
        listMercado =["papa", "trigo", "maíz"]
        def eliminar():
           for l in listMercado:
               print(f"casa {l}")
        self.titulo = tk.Label(self.raiz, text="Hola loca")
        self.titulo.pack(side=TOP, fill=X)



        self.generarALeatoreo = tk.Button(self.raiz, text="Generar", bd=0, command=eliminar)
        self.generarALeatoreo.config(pady=13, padx=29, bg="#08d945", fg="GREEN")
        self.generarALeatoreo.pack(side=TOP)

        self.raiz.mainloop()


def main():
    mi_app = aplicacion()
    return 0


if __name__ == '__main__':
    main()