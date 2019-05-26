# TODO: Mejorar BASE_SVG y LINE para pertenecer a la clase dibujar
BASE_SVG = """<svg viewBox="-50 -150 300 200" xmlns="http://www.w3.org/2000/svg">
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
                    self.lineas.append(nueva_linea)
                    f.write(BASE_SVG.format('\n'.join(self.lineas)))
        except:
            with open(destino, 'w') as arch:
                nueva_linea = LINE.format(x1, y1, x2, y2, ancho, color)
                arch.write(BASE_SVG.format(nueva_linea))
        self.vector_anterior = vector

    def _terminar_dibujo(self):
        self.lineas = []


# TODO: Remover estas pruebas y concentrarlas en un archivo test_
d = Dibujar('../svg/prueba.svg')

d.dibujar_svg((10, 0))
d.dibujar_svg((10, -10), ancho="3", color='red')
d.dibujar_svg((0, -10))
d.dibujar_svg((0, 0), color='blue')
d.cambiar_archivo('../svg/prueba2.svg')
d.dibujar_svg((10, 0))
d.dibujar_svg((10, -10), ancho="3", color='red')
