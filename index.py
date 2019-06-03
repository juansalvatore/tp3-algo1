import sys
from estructuras.Dibujar import Dibujar
from estructuras.Pluma import Pluma
from estructuras.Tortuga import Tortuga
from estructuras.SistemaL import SistemaL
from estructuras_aux.Pila import Pila
from helper.constantes import *


def main():
    try:
        if len(sys.argv) == 3:
            ruta_archivo, ruta_svg = sys.argv[1], sys.argv[2]
    except Exception:
        raise Exception(
            "error: el programa se debe ejecutar de la forma: python3 <nombre_archivo> <ruta_sistema_sl> <nombre_svg>")

    camino, angulo_constante = SistemaL(ruta_archivo).generar()
    p = Pluma()
    d = Dibujar(ruta_svg)
    pila_tortugas = Pila()
    pila_tortugas.apilar(Tortuga(angulo=90))

    def avanzar_sin_escribir(x):
        p.pluma_arriba()
        pila_tortugas.ver_tope().avanzar(x)
        p.pluma_abajo()

    OPERACIONES = {
        AVANZAR_F: lambda x: pila_tortugas.ver_tope().avanzar(x),
        AVANZAR_G: lambda x: pila_tortugas.ver_tope().avanzar(x),
        AVANZAR_SIN_ESCRIBIR_F: lambda x: avanzar_sin_escribir(x),
        AVANZAR_SIN_ESCRIBIR_G: lambda x: avanzar_sin_escribir(x),
    }

    unidad = 10
    colors = ['black', 'red', 'green', 'yellow', 'violet', 'blue']
    color_index = 0
    for operacion in camino:
        if operacion == GIRAR_DERECHA:
            print('Girar derecha', pila_tortugas.ver_tope().get_angulo())
            pila_tortugas.ver_tope().derecha(angulo_constante)
            continue
        elif operacion == GIRAR_IZQUIERDA:
            print('Girar izquierda', pila_tortugas.ver_tope().get_angulo())
            pila_tortugas.ver_tope().izquierda(angulo_constante)
            continue
        elif operacion == GIRAR_180:
            pila_tortugas.ver_tope().izquierda(angulo_constante)
            continue
        elif operacion == APILAR:
            print('----- Apilar -----')
            color_index += 1
            p.set_color(colors[color_index % len(colors)])
            if pila_tortugas.esta_vacia():
                t = Tortuga(angulo=angulo_constante)
            else:
                print(pila_tortugas.ver_tope().get_angulo())
                t = Tortuga(posicion=pila_tortugas.ver_tope().get_posicion(),
                            angulo=pila_tortugas.ver_tope().get_angulo())
                pila_tortugas.apilar(t)
            continue
        elif operacion == DESAPILAR:
            print('----- Desapilar -----')
            p.set_color('blue')
            pila_tortugas.desapilar()
            d.actualizar_vector_anterior(
                pila_tortugas.ver_tope().get_posicion())
            continue
        if operacion in OPERACIONES:
            vector = OPERACIONES[operacion](unidad)
            d.dibujar_svg(vector, 1, p.get_color())


main()
