
class SistemaL:
    ''' Representación del SistemaL'''

    def __init__(self, arch):
        self.angulo = 0
        self.axioma = ''
        self.reglas = {}
        self.archivo = arch

    def generar(self):
        ''''''
        self._procesar_archivo(self.archivo)
        return self._generar_camino(self.axioma)

    def _procesar_archivo(self, arch):
        ''' Recibe un archivo, itera las primeras dos filas del mismo. Y llama a otro método que normalice
            las reglas '''
        try:
            with open(arch, 'r') as archivo:
                self.angulo = int(next(archivo).rstrip('\n'))
                self.axioma = next(archivo).rstrip('\n')
                self._normalizar_reglas(archivo)
        except IOError as err:
            return err

    def _normalizar_reglas(self, archivo):
        ''' Recibe un archivo ya iterado dos posiciones, que solo tiene que iterar sobre las reglas.
            Usa el atributo self.reglas como diccionario para guardar { 'caracter': 'regla' } '''
        for regla in archivo:
            caracter, regla = regla.rstrip('\n').split(' ')
            self.reglas[caracter] = regla

    def _generar_camino(self, resultado, iteracion=4):
        ''' Método recursivo para la generación del camino que recorrerán las tortugas utilizadas '''
        if iteracion > 0:
            nueva_cadena = ''
            for letra in resultado:
                if letra in self.reglas:
                    nueva_cadena += self.reglas[letra]
                else:
                    nueva_cadena += letra
            resultado = nueva_cadena
            print(resultado)
            return self._generar_camino(resultado, iteracion-1)
        return resultado, self.angulo
    
    def _generar_camino_iterativo(self, resultado, iteracion=10):
        ''' Método iterativo para la generación del camino que recorrerán las tortugas utilizadas '''
        cadena = self.axioma
        cadena_por_regla = []
        while iteraciones == 0:
            for char in cadena:
                cadena_por_regla.append(self.reglas[char])
            cadena = ''.join(cadena_por_regla)
            cadena_por_regla = []
            iteraciones -= 1