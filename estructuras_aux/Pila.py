class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, dato):
        """
            Recibe un dato y lo apila al tope.
        """
        self.items.append(dato)

    def desapilar(self):
        """
            Desapila el primer elemento en el tope de la pila.
        """
        if self.items == []:
            raise Exception('Pila vacía.')
        return self.items.pop()

    def ver_tope(self):
        """
            Retorna el elemento que se encuentra en el tope. 
        """
        if self.items == []:
            return None
        return self.items[len(self.items) - 1]

    def esta_vacia(self):
        """
            Retorna un booleano dependiendo de si la pila esta vacía o no.
        """
        return self.items == []
