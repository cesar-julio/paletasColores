# ========================================
# = LOS COMPONETES GRAFICOS DEL PROGRAMA =
# ========================================

# ====== importaciones =======
from tkinter import *
from tkinter import ttk
from random import randint

import tkinter as tk
import tkinter.font as tkFont

tarjetas = []  # LISTA DE TARJETAS DE COLORES
lisNombres = []  # Nombres de la lista
listNombreColores = []

# ======= COLORES DE LA INTERFAZ GRAFICA ========
coloresFondoGris = "DIMGRAY"
colorTextBoton1 = "WHITE"
colorTextBoton2 = "#08d945"

numeroDeMuestra = 5


# ======== componetes del inico =======
def de_inicio(self, ubucacion):
    # ===== variables ===
    self.fuenteTitulo = tkFont.Font(family="Helvetica", size=9)
    self.fuenteBotones = tkFont.Font(family="Console", size=10)
    self.fuenteNombreColores = tkFont.Font(family="Console", size=7)

    self.contPadre = tk.Frame(ubucacion, bg=coloresFondoGris)
    self.contPadre.pack(side=TOP, pady=5, padx=5)

    self.contNavegadorColor = tk.Frame(self.contPadre, bg=coloresFondoGris)
    self.contNavegadorColor.pack(side=LEFT, fill=Y)

    self.contMuestra = tk.Frame(self.contNavegadorColor)
    self.contMuestra.config(bg=coloresFondoGris)
    self.contMuestra.grid(column=0, row=0, columnspan=2)

    # ========= función que gera los colores ========
    opciones_colores(self, self.contNavegadorColor)
    # ===============================================
    generar_componetes_muestra(self)

    self.contPaletasColores = tk.Frame(self.contPadre, bg=coloresFondoGris)
    self.contPaletasColores.pack(side=RIGHT, fill=Y, padx=10)

    coloresLista = ["#212530", "#67918F", "#965600", "#F1C063"]
    for e in range(4):
        self.e = tk.Label(self.contPaletasColores, width=2, height=1)
        self.e.config(bg=coloresLista[e])
        self.e.grid(column=0, row=e, padx=2, pady=2)

    self.prueva = tk.Canvas(self.contPaletasColores, width=20, height=20, bg="BLUE")
    self.prueva.grid(column=0, row=4)


def crear_tarjetas(self):
        for tarjeta in range(numeroDeMuestra):
            listNombreColores.append(colores_aleatorio())

            self.tarjeta = tk.Button(self.contMuestra, width=5, height=5, bd=False, )
            self.tarjeta.config(background=listNombreColores[tarjeta])
            tarjetas.append(self.tarjeta)  # agregar las trajetas a la lista

def crear_nombre_colores(self):
        for nombres in range(numeroDeMuestra):
            self.nombres = tk.Label(self.contMuestra, text=listNombreColores[nombres])
            self.nombres.config(font=self.fuenteNombreColores, bg=coloresFondoGris)
            lisNombres.append(self.nombres)

def generar_componetes_muestra(self):


    if len(tarjetas) == 0 and len(lisNombres) == 0:
        print(f"soy el numero de tarjetas {len(tarjetas)}")
        crear_tarjetas(self)
        crear_nombre_colores(self)
        colocar_tarjetas()
    else:
        print(f"soy el numero de tarjetas {len(tarjetas)}")
        tarjetas.clear()
        lisNombres.clear()
        crear_tarjetas(self)
        crear_nombre_colores(self)
        colocar_tarjetas()




obtenerCatidad = object

def opciones_colores(self, contenedor):
    self.contControles = tk.Frame(contenedor, bg=coloresFondoGris, bd=0)
    self.contControles.grid(column=0, row=4, padx=10, pady=10)

    self.contNumLista = tk.Frame(self.contControles, pady=2)
    self.contNumLista.grid(column=1, row=0, rowspan=2, padx=10)

    self.nColoresTitulo = tk.Label(self.contNumLista, text="N° colores", font=self.fuenteTitulo, justify=CENTER)
    self.nColoresTitulo.pack(side=TOP)

    self.cantidadColores = ttk.Combobox(self.contNumLista, state="readonly", width=5)
    self.cantidadColores["values"] = [5, 10, 15, 20]
    self.cantidadColores.current(0)
    self.cantidadColores.pack(side=TOP)

    global obtenerCatidad
    obtenerCatidad = self.cantidadColores

    def generar_nuevos_colores():
        global numeroDeMuestra
        numeroDeMuestra = int(obtenerCatidad.get())

        generar_componetes_muestra(self)


        #===== vaciar la lista de colores
        listNombreColores.clear()

        ind = 0
        for elm in tarjetas:
            listNombreColores.append(colores_aleatorio())
            elm.config(background=listNombreColores[ind])
            ind += 1
        inx = 0
        for lb in lisNombres:
            lb.config(text=listNombreColores[inx])
            inx += 1


    self.generarALeatoreo = tk.Button(self.contControles, text="Generar", bd=0, command=generar_nuevos_colores)
    self.generarALeatoreo.config(font=self.fuenteBotones, pady=13, padx=29, bg="#08d945", fg=colorTextBoton1)
    self.generarALeatoreo.grid(column=0, row=0, rowspan=2)





#  Función para coambiar los colores aleatoreos del boton



# ===== Generar los colores aleatorios ======
def colores_aleatorio():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    colorInicio = "#%02x%02x%02x" % (R, G, B)
    return colorInicio


def colocar_tarjetas():
    posicionRowT = 0
    posicionRowL = 1

    posicionColumnT = 0
    posicionColumnL = 0

    numeroElementos = 0
    for elmet in tarjetas:
        if numeroElementos == 5:
            posicionRowT += 2
            posicionColumnT = 0
        elif numeroElementos == 10:
            posicionRowT += 2
            posicionColumnT = 0
        elif numeroElementos == 15:
            posicionRowT += 2
            posicionColumnT = 0
        elmet.grid(column=posicionColumnT, row=posicionRowT)

        posicionColumnT += 1
        if numeroElementos < len(tarjetas):
            numeroElementos += 1
        else:
            break

    numeroNombres = 0
    for nombr in lisNombres:
        if numeroNombres == 5:
            posicionRowL += 2
            posicionColumnL = 0
        elif numeroNombres == 10:
            posicionRowL += 2
            posicionColumnL = 0
        elif numeroNombres == 15:
            posicionRowL += 2
            posicionColumnL = 0
        nombr.grid(column=posicionColumnL, row=posicionRowL)

        posicionColumnL += 1
        if numeroNombres < len(lisNombres):
            numeroNombres += 1
        else:
            break