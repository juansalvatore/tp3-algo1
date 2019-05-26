import unittest
from Tortuga import Tortuga


class TestTortuga(unittest.TestCase):
    def setUp(self):
        """
            Instancia la clase Tortuga.
        """
        print('\nsetUp')
        self.t = Tortuga()

    def test_girar_izquierda(self):
        """ La tortuga gira en un cuadrado de 10x10 a la izquierda. """
        print('test_girar_izquierda')
        t = self.t
        self.assertEqual(t.avanzar(10), (10, 0))
        t.izquierda(90)
        self.assertEqual(t.avanzar(10), (10, -10))
        t.izquierda(90)
        self.assertEqual(t.avanzar(10), (0, -10))
        t.izquierda(90)
        self.assertEqual(t.avanzar(10), (0, 0))
        t.izquierda(90)

    def test_girar_derecha(self):
        """ La tortuga gira en un cuadrado de 10x10 hacia la derecha. """
        print('test_girar_derecha')
        t = self.t
        t.derecha(90)
        self.assertEqual(t.avanzar(10), (0, 10))
        t.derecha(90)
        self.assertEqual(t.avanzar(10), (-10, 10))
        t.derecha(90)
        self.assertEqual(t.avanzar(10), (-10, 0))
        t.derecha(90)
        self.assertEqual(t.avanzar(10), (0, 0))


if __name__ == '__main__':
    unittest.main()
