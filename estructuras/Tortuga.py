from math import cos, sin, radians, floor, ceil
from Pluma import Pluma


class Tortuga:
    ''' Representacion del elemento que realiza graficas Tortuga. (FALTA DOCUMENTAR COMANDOS) '''

    def __init__(self, posicion=(0, 0), v_director=(1, 0),  angulo=0):
        self.posicion = posicion
        self.v_director = v_director
        self.angulo = angulo
        self.pluma = Pluma()

    def avanzar(self, n=1):
        ''' Avanza una cantidad n, pasada por parametro '''
        x_pos, y_pos = self.posicion
        x_dir, y_dir = self._calc_vector_director()
        self.posicion = ((x_dir * n) + x_pos, (y_dir * n) + y_pos)
        return self.posicion

    def izquierda(self, angulo):
        self.angulo += angulo % 360
        if self.angulo == 360:
            self.angulo = 0

    def derecha(self, angulo):
        self.angulo -= angulo % 360
        if self.angulo == 360:
            self.angulo = 0

    def _calc_vector_director(self):
        x, y = self.v_director
        cos_angle = round(cos(radians(self.angulo)))
        sin_angle = round(sin(radians(self.angulo)))
        if self.angulo < 180:
            nuevo_x = x * cos_angle - y * sin_angle
            nuevo_y = x * sin_angle + y * cos_angle
        else:
            nuevo_x = x * cos_angle + y * sin_angle
            nuevo_y = x * sin_angle - y * cos_angle
        return nuevo_x, nuevo_y

    def __str__(self):
        x, y = self.posicion
        return f'posicion: ({x},{y}), angulo: {self.angulo}'


def test():
    t = Tortuga()
    print(1, t.avanzar(10))
    t.izquierda(90)
    print(2, t.avanzar(10))
    t.izquierda(90)
    print(3, t.avanzar(10))
    t.izquierda(90)
    print(4, t.avanzar(10))
    t.izquierda(90)

    print("\n-------------\n")

    t.derecha(90)
    print(1, t.avanzar(10))
    t.derecha(90)
    print(2, t.avanzar(10))
    t.derecha(90)
    print(3, t.avanzar(10))
    t.derecha(90)
    print(4, t.avanzar(10))


test()
