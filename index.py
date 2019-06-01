import sys
from estructuras.Dibujar import Dibujar
from estructuras.Pluma import Pluma
from estructuras.Tortuga import Tortuga
from estructuras.SistemaL import SistemaL
from estructuras_aux.Pila import Pila


class Main:
    def __init__(self):
        self.ruta_archivo, self.ruta_svg = sys.argv[1], sys.argv[2]
        self.camino, self.angulo = SistemaL(self.ruta_archivo).generar()

        self.t = Tortuga(angulo=self.angulo)
        self.p = Pluma()
        self.d = Dibujar(self.ruta_svg)

        self.tortugas = Pila()
        self.angulos = Pila()

        self.tortugas.apilar(self.t)
        self.angulos.apilar(self.angulo)

        self.OPERACIONES = {
            'F': lambda x: self.t.avanzar(x),
            'G': lambda x: self.t.avanzar(x),
            'f': lambda x: self.avanzar_sin_escribir(x),
            'g': lambda x: self.avanzar_sin_escribir(x),
            '+': lambda ang: self.t.derecha(ang),
            '-': lambda ang: self.t.izquierda(ang),
            '|': lambda ang: self.t.izquierda(ang),  # usar derecha seria lo mismo
            '[': lambda x: self.apilar_tortuga(),
            ']': lambda x: self.desapilar_tortuga()
        }
        self.procesar()

    def procesar(self):
        unidad = 4
        for operacion in self.camino:
            if operacion == '+' or operacion == '-':
                self.OPERACIONES[operacion](self.angulo)
                continue
            elif operacion == '|':
                self.OPERACIONES[operacion](180)
                continue
            elif operacion == '[' or operacion == ']':
                self.OPERACIONES[operacion](self.tortugas)
                continue
            if operacion in self.OPERACIONES:
                vector = self.OPERACIONES[operacion](unidad)
                self.d.dibujar_svg(vector)

    def avanzar_sin_escribir(self, x):
        self.p.pluma_arriba()
        self.t.avanzar(x)
        self.p.pluma_abajo()

    def apilar_tortuga(self):
        t = Tortuga(angulo=self.angulo)
        self.tortugas.apilar(t)
        self.angulos.apilar(self.angulos)

    def desapilar_tortuga(self):
        self.tortugas.desapilar()
        self.angulos.desapilar()

Main()