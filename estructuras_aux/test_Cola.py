import unittest
from Cola import Cola

# TODO: usar str(c) para comparar strigns en vez de acceder a self.items
# para prevenir error si se cambia la logica de la cola para usar nodos
# en vez de un array


class TestCola(unittest.TestCase):
    def setUp(self):
        """
            Instancia la clase Cola.
        """
        print('\nsetUp')
        self.c = Cola()

    def test_encolar(self):
        """
            Agrega un nuevo elemento al frente.
        """
        print('test_encolar')

        c = self.c
        c.encolar(1)
        self.assertEqual(c.items, [1])
        c.encolar(2)
        self.assertEqual(c.items, [2, 1])
        c.encolar(3)
        self.assertEqual(c.items, [3, 2, 1])

    def test_desencolar(self):
        """
            Desencola el primer elemento.
        """
        print('test_desencolar')

        c = self.c
        c.encolar(1)
        c.encolar(2)
        c.encolar(3)
        self.assertEqual(c.desencolar(), 1)
        self.assertEqual(c.desencolar(), 2)
        self.assertEqual(c.desencolar(), 3)
        with self.assertRaises(Exception) as context:
            c.desencolar()
        self.assertTrue('Cola vacía.' in str(context.exception))

    def test_esta_vacia(self):
        """
            Chequea si la cola esta o no vacía.
        """
        print('test_esta_vacia')
        c = self.c
        self.assertEqual(c.esta_vacia(), True)
        c.encolar(1)
        self.assertEqual(c.esta_vacia(), False)
        c.desencolar()
        self.assertEqual(c.esta_vacia(), True)

    def test_ver_frente(self):
        """
            Retorna el primer elemento manteniendo la cola intacta.
        """
        print('test_ver_frente')

        c = self.c
        self.assertEqual(c.ver_frente(), None)
        c.encolar(1)
        c.encolar(2)
        self.assertEqual(c.ver_frente(), 1)
        c.desencolar()
        self.assertEqual(c.ver_frente(), 2)


if __name__ == '__main__':
    unittest.main()
