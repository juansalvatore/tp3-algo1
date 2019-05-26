from estructuras_aux.Cola import Cola
from estructuras_aux.Pila import Pila
from Tortuga import Tortuga

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
        
        self.procesar_archivo(arch)
        self.dibujar()

    def procesar_archivo(self, arch):
        ''' Recibe un archivo, itera las primeras dos filas del mismo. Y llama a otro método que normalice
            las reglas '''
        try:
            with open(arch, 'r') as archivo:
                self.angulo = float(next(archivo).rstrip('\n'))
                self.axioma = next(archivo).rstrip('\n')
                self._normalizar_reglas(archivo)
        except IOError as err:
            return err
    
    def dibujar(self):
        ''' Empieza el dibujo de la tortuga '''
        tortuga = Tortuga()
        

    def _normalizar_reglas(self, archivo):
        ''' Recibe un archivo ya iterado dos posiciones, que solo tiene que iterar sobre las reglas.
            Usa el atributo self.reglas como diccionario para guardar { 'caracter': 'regla' } '''
        for regla in archivo:
            caracter, regla = regla.rstrip('\n').split(' ')
            self.reglas[caracter] = regla
    
    def _generar_camino(self, resultado, iteracion = 20):
        ''' Método recursivo para la generación del camino que recorrerán las tortugas utilizadas '''
        if iteracion > 0:
            nueva_cadena = ''
            for letra in resultado:
                if letra in self.reglas:
                    nueva_cadena += self.reglas[letra]
                else:
                    nueva_cadena += letra
            resultado = nueva_cadena
            return self._generar_camino(resultado, iteracion-1)
        return resultado

    def _apilar(self):
        pass

    def _desapilar(self):
        pass

        
