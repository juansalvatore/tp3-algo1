import sys
from estructuras.Dibujar import Dibujar
from estructuras.Pluma import Pluma
from estructuras.Tortuga import Tortuga
from estructuras.SistemaL import SistemaL
from estructuras_aux.Pila import Pila
from helper.constantes import *


class Main:
    def __init__(self):
        try:
            self.ruta_archivo, self.ruta_svg = self._validar_entrada()
        except IndexError as err:
            print(err)
            return None
        self.camino, self.angulo = SistemaL(self.ruta_archivo).generar()
        self.p = Pluma()
        self.d = Dibujar(self.ruta_svg)
        self.tortugas = Pila()
        self.apilar_tortuga()

        self.OPERACIONES = {
            AVANZAR_F: lambda x: self.tortugas.ver_tope().avanzar(x),
            AVANZAR_G: lambda x: self.tortugas.ver_tope().avanzar(x),
            AVANZAR_SIN_ESCRIBIR_F: lambda x: self.avanzar_sin_escribir(x),
            AVANZAR_SIN_ESCRIBIR_G: lambda x: self.avanzar_sin_escribir(x),
            GIRAR_DERECHA: lambda ang: self.tortugas.ver_tope().derecha(ang),
            GIRAR_IZQUIERDA: lambda ang: self.tortugas.ver_tope().izquierda(ang),
            # usar derecha seria lo mismo
            GIRAR_180: lambda ang: self.tortugas.ver_tope().izquierda(ang),
            APILAR: lambda x: self.apilar_tortuga(),
            DESAPILAR: lambda x: self.desapilar_tortuga()
        }
        self.procesar()

    def procesar(self):
        unidad = 4
        for operacion in self.camino:
            if operacion == GIRAR_DERECHA or operacion == GIRAR_IZQUIERDA:
                self.OPERACIONES[operacion](self.angulo)
                continue
            elif operacion == GIRAR_180:
                self.OPERACIONES[operacion](180)
                continue
            elif operacion == APILAR or operacion == DESAPILAR:
                self.OPERACIONES[operacion](self.tortugas)
                continue
            if operacion in self.OPERACIONES:
                vector = self.OPERACIONES[operacion](unidad)
                self.d.dibujar_svg(vector)

    def avanzar_sin_escribir(self, x):
        self.p.pluma_arriba()
        self.tortugas.ver_tope().avanzar(x)
        self.p.pluma_abajo()

    def apilar_tortuga(self):
        t = Tortuga(angulo=self.angulo)
        self.tortugas.apilar(t)

    def desapilar_tortuga(self):
        self.tortugas.desapilar()
        self.d.actualizar_vector_anterior((0, 0))
        # self.tortugas.ver_tope().get_posicion()

    def _validar_entrada(self):
        if len(sys.argv) == 3:
            return sys.argv[1], sys.argv[2]
        raise IndexError(
            "error: el programa se debe ejecutar de la forma: python3 <nombre_archivo> <ruta_sistema_sl> <nombre_svg>")


Main()
