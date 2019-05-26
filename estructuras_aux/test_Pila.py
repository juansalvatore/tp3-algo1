import unittest
from Pila import Pila

# TODO: usar str(p) para comparar strigns en vez de acceder a self.items
# para prevenir error si se cambia la logica de la pila para usar nodos
# en vez de un array


class TestPila(unittest.TestCase):
    def setUp(self):
        """
            Instancia la clase Pila.
        """
        print('\nsetUp')
        self.p = Pila()

    def test_apilar(self):
        """
            Apila un nuevo elemento al tope.
        """
        print('test_apilar')

        p = self.p
        p.apilar(1)
        self.assertEqual(p.items, [1])
        p.apilar(2)
        self.assertEqual(p.items, [1, 2])
        p.apilar(3)
        self.assertEqual(p.items, [1, 2, 3])

    def test_desapilar(self):
        """
            Desapila el primer elemento.
        """
        print('test_desapilar')

        p = self.p
        p.apilar(1)
        p.apilar(2)
        p.apilar(3)
        self.assertEqual(p.desapilar(), 3)
        self.assertEqual(p.desapilar(), 2)
        self.assertEqual(p.desapilar(), 1)
        with self.assertRaises(Exception) as context:
            p.desapilar()
        self.assertTrue('Pila vacía.' in str(context.exception))

    def test_esta_vacia(self):
        """
            Chequea si la pila esta o no vacía.
        """
        print('test_esta_vacia')
        p = self.p
        self.assertEqual(p.esta_vacia(), True)
        p.apilar(1)
        self.assertEqual(p.esta_vacia(), False)
        p.desapilar()
        self.assertEqual(p.esta_vacia(), True)

    def test_ver_tope(self):
        """
            Retorna el primer elemento manteniendo la pila intacta.
        """
        print('test_ver_tope')

        p = self.p
        self.assertEqual(p.ver_tope(), None)
        p.apilar(1)
        p.apilar(2)
        self.assertEqual(p.ver_tope(), 2)
        p.desapilar()
        self.assertEqual(p.ver_tope(), 1)


if __name__ == '__main__':
    unittest.main()
