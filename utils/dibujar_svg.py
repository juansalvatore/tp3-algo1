BASE_SVG = """<svg viewBox="-50 -150 300 200" xmlns="http://www.w3.org/2000/svg">
    {}
</svg>
"""
LINE = """<line x1="{}" y1="{}" x2="{}" y2="{}" stroke-width="{}" stroke="{}" />"""


class Dibujar:
    def __init__(self):
        self.lineas = []
        self.vector_anterior = (0, 0)

    def dibujar_svg(self, destino, vector, ancho=1, color="black"):
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


d = Dibujar()

d.dibujar_svg('../svg/prueba.svg', (10, 0))
d.dibujar_svg('../svg/prueba.svg', (10, -10), color='red')
d.dibujar_svg('../svg/prueba.svg', (0, -10))
d.dibujar_svg('../svg/prueba.svg', (0, 0), color='blue')
