class Pluma:
    ''' Representacion de una pluma '''

    def __init__(self, color="black", ancho=1):
        self.ancho = ancho
        self.escribir = True
        self.color = color

    def pluma_arriba(self):
        ''' La pluma deja de escribir '''
        self.escribir = False

    def pluma_abajo(self):
        ''' Permite que la pluma escriba '''
        self.escribir = True

    def get_color(self):
        ''' Devuelve el color asignado a la pluma '''
        return self.color

    def set_color(self, color):
        ''' Dado un color, modifica el color de la pluma. Devuelve el nuevo color '''
        self.color = color
        return self.color

    def get_ancho(self):
        ''' Devuelve el ancho asignado a la pluma '''
        return self.ancho

    def set_ancho(self, ancho):
        ''' Dado un ancho, modifica el ancho de la pluma. Devuelve el nuevo ancho '''
        self.ancho = ancho
        return self.ancho
