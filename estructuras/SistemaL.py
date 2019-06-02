
class SistemaL:
    ''' Representación del SistemaL'''

    def __init__(self, arch):
        self.angulo = 0
        self.axioma = ''
        self.reglas = {}
        self.archivo = arch

    def generar(self):
        ''' Inicia el proceso del archivo pasado como parámetro al SistemaL. Finalizado el proceso
            del archivo, genera el camino que recorrerá la tortuga. '''
        self._procesar_archivo(self.archivo)
        return self._generar_camino_iterativo(self.axioma)

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
    
    def _generar_camino_iterativo(self, cadena, iteracion=6):
        ''' Método iterativo para la generación del camino que recorrerán las tortugas utilizadas '''
        cadena_por_regla = []
        while iteracion > 1:
            for letra in cadena:
                if letra in self.reglas:
                    cadena_por_regla += self.reglas[letra]
                else:
                    cadena_por_regla += letra
            cadena = ''.join(cadena_por_regla)
            cadena_por_regla = []
            iteracion -= 1
        return cadena, self.angulo