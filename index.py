import sys
from estructuras.Dibujar import Dibujar
from estructuras.Pluma import Pluma
from estructuras.Tortuga import Tortuga
from estructuras.SistemaL import SistemaL


def main():
    ruta_archivo, ruta_svg = sys.argv[1], sys.argv[2]
    camino, angulo = SistemaL(ruta_archivo).generar()

    t = Tortuga(angulo=angulo)
    p = Pluma()
    d = Dibujar(ruta_svg)

    def avanzar_sin_escribir(x):
        p.pluma_arriba()
        t.avanzar(x)
        p.pluma_abajo()

    OPERACIONES = {
        'F': lambda x: t.avanzar(x),
        'G': lambda x: t.avanzar(x),
        'f': lambda x: avanzar_sin_escribir(x),
        'g': lambda x: avanzar_sin_escribir(x),
        '+': lambda ang: t.derecha(ang),
        '-': lambda ang: t.izquierda(ang),
        '|': lambda ang: t.izquierda(ang),  # usar derecha seria lo mismo
        # '[': lambda x: print('['),
        # ']': lambda x: print(']').
    }

    unidad = 4
    for operacion in camino:
        if operacion == '+' or operacion == '-':
            OPERACIONES[operacion](angulo)
            continue
        elif operacion == '|':
            OPERACIONES[operacion](180)
            continue
        if operacion in OPERACIONES:
            vector = OPERACIONES[operacion](unidad)
            d.dibujar_svg(vector)


main()
