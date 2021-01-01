from tkinter import *
import componetes

import  tkinter as tk


class aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("COLOR")
        self.raiz.resizable(width=False, height=False)
        self.raiz.config(bg="DIMGRAY")
#        self.raiz.iconphoto(False, tk.PhotoImage(file='img/icon.png'))

        #===== componetes graficos =====
        componetes.de_inicio(self, self.raiz)

        self.raiz.mainloop()
def main():
    mi_app = aplicacion()
    return 0

if __name__ == '__main__':
    main()
