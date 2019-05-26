class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, dato):
        """
            Agrega el dato al final de la cola.
        """
        self.items = [dato] + self.items

    def desencolar(self):
        """
            Desencola el primer elemento que fue encolado y retorna el dato desencolado.
        """
        if self.items == []:
            raise Exception('Cola vacía.')
        return self.items.pop()

    def ver_frente(self):
        """
            Retorna el frente de la cola
        """
        if self.items == []:
            return None
        return self.items[len(self.items) - 1]

    def esta_vacia(self):
        """
            Retorna si la cola esta o no vacía.
        """
        return self.items == []
