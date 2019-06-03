import sys
from estructuras.Dibujar import Dibujar
from estructuras.Pluma import Pluma
from estructuras.Tortuga import Tortuga
from estructuras.SistemaL import SistemaL
from estructuras_aux.Pila import Pila
from constantes import *


def main():
    ''' Inicia el proceso de generación de imágenes fractales.
        comando: python3 <nombre_programa> <nombre_archivo_sl> <nombre_archivo_svg_destino>
        pre: el nombre archivo debe tener la ruta relativa correspondiente
    '''
    try:
        if len(sys.argv) == 3:
            ruta_archivo, ruta_svg = sys.argv[INDICE_RUTA], sys.argv[INDICE_SVG]
    except Exception:
        raise Exception("error: el programa se debe ejecutar de la forma: python3 <nombre_archivo> <ruta_sistema_sl> <nombre_svg>")

    camino, angulo_constante = SistemaL(ruta_archivo).generar()

    pluma = Pluma()
    dibujo = Dibujar(ruta_svg)
    pila_tortugas = Pila()
    pila_tortugas.apilar(Tortuga(angulo=ANGULO_INICIAL))

    color_index = COLOR_INDEX

    def avanzar_sin_escribir(x):
        pluma.pluma_arriba()
        pila_tortugas.ver_tope().avanzar(x)
        pluma.pluma_abajo()

    for operacion in camino:
        
        if operacion == GIRAR_DERECHA: girar_derecha(pila_tortugas, angulo_constante)            
        elif operacion == GIRAR_IZQUIERDA: girar_izquierda(pila_tortugas, angulo_constante)
        elif operacion == GIRAR_180: girar_izquierda(pila_tortugas, GIRO_COMPLETO)
        elif operacion == APILAR: apilar(pila_tortugas, pluma, angulo_constante, color_index)
        elif operacion == DESAPILAR: desapilar(pila_tortugas, pluma, dibujo)
        elif operacion == AVANZAR_F or operacion == AVANZAR_G: avanzar(pila_tortugas, dibujo, pluma, UNIDAD)
        elif operacion == AVANZAR_SIN_ESCRIBIR_F or operacion == AVANZAR_SIN_ESCRIBIR_G: avanzar_sin_escribir(pila_tortugas, dibujo, pluma, unidad)


def apilar(pila_tortugas, pluma, angulo_constante, color_index):
    ''' Recibe una pluma, una pila de tortugas, un índice de color.
        Apila una tortuga, con un color diferente, con el ángulo que tenía la última tortuga usada.
    '''
    print('----- Apilar -----')
    color_index += 1
    pluma.set_color(COLORS[color_index % len(COLORS)])
    if pila_tortugas.esta_vacia():
        tortuga = Tortuga(angulo=angulo_constante)
    else:
        print(pila_tortugas.ver_tope().get_angulo())
        tortuga = Tortuga(posicion=pila_tortugas.ver_tope().get_posicion(), angulo=pila_tortugas.ver_tope().get_angulo())
        pila_tortugas.apilar(tortuga)

def desapilar(pila_tortugas, pluma, dibujo):
    ''' Recibe una pluma, una pila de tortugas y un dibujo. Desapila una tortuga y la descarta.'''
    print('----- Desapilar -----')
    pluma.set_color(BLUE)
    pila_tortugas.desapilar()
    dibujo.actualizar_vector_anterior(pila_tortugas.ver_tope().get_posicion())

def girar_derecha(pila_tortugas, angulo):
    ''' Recibe una pila de tortugas y un ángulo. Y gira la tortuga'''
    print('Girar derecha', pila_tortugas.ver_tope().get_angulo())
    pila_tortugas.ver_tope().derecha(angulo)

def girar_izquierda(pila_tortugas, angulo):
    ''' Recibe una pila de tortugas y un ángulo. Y gira la tortuga'''
    pila_tortugas.ver_tope().izquierda(angulo)

def avanzar(pila_tortugas, dibujo, pluma, unidad):
    ''' Recibe una pila de tortugas, un dibujo, una pluma y una unidad. Avanza la tortuga'''
    vector = pila_tortugas.ver_tope().avanzar(unidad)
    dibujo.dibujar_svg(vector, 1, pluma.get_color())

def avanzar_sin_escribir(pila_tortugas, dibujo, pluma, unidad):
    ''' Recibe una pila de tortugas, un dibujo, una pluma y una unidad. Avanza la tortuga, sin escribir '''
    vector = pila_tortugas.ver_tope().avanzar_sin_escribir(unidad)
    dibujo.dibujar_svg(vector, 1, pluma.get_color())

main()
