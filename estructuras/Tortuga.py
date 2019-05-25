from math import cos, sin
from Pluma import Pluma


class Tortuga:
    ''' Representación del elemento que realiza gráficas Tortuga. (FALTA DOCUMENTAR COMANDOS) '''

    def __init__(self, angulo):
        self.posicion = (0, 0)
        self.vector_director = (0, 0)
        self.angulo = angulo
        self.pluma = Pluma()

    def avanzar(self, n):
        ''' Avanza una cantidad n, pasada por parámetro '''
        x, y = self.posicion
        return self.posicion

    def izquierda(self, angulo):
        self.angulo += angulo % 360
        x, y = self.vector_director
        nuevo_x = x * cos(self.angulo) - y * sin(self.angulo)
        nuevo_y = x * sin(self.angulo) + y * cos(self.angulo)
        self.vector_director = (nuevo_x, nuevo_y)

    def derecha(self, angulo):
        self.angulo -= angulo % 360
