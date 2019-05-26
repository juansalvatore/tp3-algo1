class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, dato):
        self.items = [dato] + self.items

    def desencolar(self):
        if self.items == []:
            raise Exception('Cola vacía.')
        return self.items.pop()

    def ver_frente(self):
        if self.items == []:
            raise Exception('Cola vacía.')
        return self.items[0]

    def esta_vacia(self):
        return self.items == []
