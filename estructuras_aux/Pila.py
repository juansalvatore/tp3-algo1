class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if self.items == []:
            raise Exception('Pila vacía.')
        return self.items.pop()

    def ver_tope(self):
        if self.items == []:
            return None
        return self.items[len(self.items) - 1]

    def esta_vacia(self):
        return self.items == []
