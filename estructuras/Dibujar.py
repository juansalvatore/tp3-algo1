BASE_SVG = """<svg viewBox="{} {} {} {}" xmlns="http://www.w3.org/2000/svg" style="background: white">
{}
</svg>
"""
LINE = """\t<line x1="{}" y1="{}" x2="{}" y2="{}" stroke-width="{}" stroke="{}" />"""


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
        """
            Recibe un archivo y actualiza el archivo en el cual seguir dibujando.
            Termina el dibujo.
        """
        self.archivo = archivo
        self._terminar_dibujo()

    def dibujar_svg(self, vector, ancho=1, color="black"):
        """
            Recibe un vector (Tupla R2), un ancho (Int) y el color para dibujar (Str).
            Genera un archivo svg con una linea por cada vector que recibe comenzando desde
            (0,0).
        """
        destino = self.archivo
        x1, y1 = self.vector_anterior
        x2, y2 = vector
        if x2 < self.maximo_x:
            self.maximo_x = x2
        if y2 < self.maximo_y:
            self.maximo_y = y2
        if x2 > self.minimo_x:
            self.minimo_x = x2
        if y2 > self.minimo_y:
            self.minimo_y = y2
        try:
            with open(destino) as arch:
                with open(destino, 'w') as f:
                    nueva_linea = LINE.format(x1, y1, x2, y2, ancho, color)
                    self.lineas.append(nueva_linea)
                    f.write(BASE_SVG.format(self.maximo_x - 10,
                                            self.maximo_y - 10, -1 * self.maximo_x + self.minimo_x + 20,
                                            -1 * self.maximo_y + self.minimo_y + 20, '\n'.join(self.lineas)))
        except:
            with open(destino, 'w') as arch:
                nueva_linea = LINE.format(x1, y1, x2, y2, ancho, color)
                self.lineas.append(nueva_linea)
                arch.write(BASE_SVG.format(self.maximo_x - 10,
                                           self.maximo_y - 10, -1 * self.maximo_x + self.minimo_x + 20,
                                           -1 * self.maximo_y + self.minimo_y + 20, '\n'.join(self.lineas)))
        self.vector_anterior = vector

    def _terminar_dibujo(self):
        """
            Borra las lineas guardadas en el arreglo self.lineas para comenzar a 
            escribir de cero.
        """
        self.lineas = []

    def actualizar_vector_anterior(self, nuevo_vector):
        """
            Recibe un nuevo vector y actualiza el vector anterior, el cual representa desde
            que posición se dibujará la linea siguiente.
        """
        self.vector_anterior = nuevo_vector
