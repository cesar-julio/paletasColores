from tkinter import *
from tkinter import ttk
import componetes


class aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Pale color")
        self.raiz.resizable(width=False, height=False)
        self.raiz.config(bg="DIMGRAY")

        #===== componetes graficos =====
        componetes.de_inicio(self, self.raiz)

        self.raiz.mainloop()
def main():
    mi_app = aplicacion()
    return 0

if __name__ == '__main__':
    main()