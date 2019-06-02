# TODO: Mejorar BASE_SVG y LINE para pertenecer a la clase dibujar
# x-mínimo, y-mínimo, ancho y alto
BASE_SVG = """<svg viewBox="{} {} {} {}" xmlns="http://www.w3.org/2000/svg" style="background: white">
{}
</svg>
"""
LINE = """\t<line x1="{}" y1="{}" x2="{}" y2="{}" stroke-width="{}" stroke="{}" />"""

# TODO: Testear y documentar clase


class Dibujar:
    def __init__(self, archivo):
        self.archivo = archivo
        self.lineas = []
        self.vector_anterior = (0, 0)
        self.maximo_x = 0
        self.maximo_y = 0
        self.minimo_x = 0
        self.minimo_y = 0

    def cambiar_archivo(self, archivo):
        self.archivo = archivo
        self._terminar_dibujo()

    def dibujar_svg(self, vector, ancho=1, color="black"):
        destino = self.archivo
        x1, y1 = self.vector_anterior
        x2, y2 = vector
        try:
            with open(destino) as arch:
                with open(destino, 'w') as f:
                    nueva_linea = LINE.format(x1, y1, x2, y2, ancho, color)
                    if x2 < self.maximo_x:
                        self.maximo_x = x2
                    if y2 < self.maximo_y:
                        self.maximo_y = y2
                    if x2 > self.minimo_x:
                        self.minimo_x = x2
                    if y2 > self.minimo_y:
                        self.minimo_y = y2
                    self.lineas.append(nueva_linea)
                    f.write(BASE_SVG.format(self.maximo_x - 10,
                                            self.maximo_y - 10, -1 * self.maximo_x + self.minimo_x + 20,
                                            -1 * self.maximo_y + self.minimo_y + 20, '\n'.join(self.lineas)))
        except:
            with open(destino, 'w') as arch:
                nueva_linea = LINE.format(x1, y1, x2, y2, ancho, color)
                arch.write(BASE_SVG.format(nueva_linea))
        self.vector_anterior = vector

    def _terminar_dibujo(self):
        self.lineas = []


# TODO: Remover estas pruebas y concentrarlas en un archivo test_
# d = Dibujar('../svg/prueba.svg')

# d.dibujar_svg((10, 0))
# d.dibujar_svg((10, -10), ancho="3", color='blue')
# d.dibujar_svg((0, -10))
# d.dibujar_svg((0, 0), color='blue')
# d.cambiar_archivo('../svg/prueba2.svg')
# d.dibujar_svg((10, 0))
# d.dibujar_svg((10, -10), ancho="3", color='red')
