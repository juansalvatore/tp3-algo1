class SistemaL:
    ''' Representación del SistemaL'''

    def __init__(self, arch):
        self.angulo = 0
        self.axioma = ''
        self.reglas = {}
        self.operaciones = {
            'F': 'avanzar',
            'G': 'avanzar',
            'f': 'avanzar_sin_escribir',
            'g': 'avanzar_sin_escribir',
            '+': 'derecha',
            '-': 'izquierda',
            '|': 'invertir_dir',
            '[': 'apilar',
            ']': 'desapilar'
        }
        self.pila_tortugas = Pila()
        self.camino = Cola()

    def apilar(self):
        pass

    def desapilar(self):
        pass

    def procesar_archivo(self, arch):
        pass

    def generar_camino(self):
        pass

    def dibujar(self):
        pass
