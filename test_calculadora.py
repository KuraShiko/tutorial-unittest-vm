
import unittest
from calculadora import sumar 
class TestCalculadora(unittest.TestCase):
    """Clase de pruebas para la función sumar."""

    def test_sumar_enteros_positivos(self):
        """Prueba la suma de dos números enteros positivos."""
        self.assertEqual(sumar(5, 10), 15)

    def test_sumar_flotantes(self):
        """Prueba la suma de dos números de punto flotante."""
        self.assertEqual(sumar(3.5, 2.5), 6.0)

    def test_sumar_con_un_negativo(self):
        """Prueba la suma de un número positivo y uno negativo."""
        self.assertEqual(sumar(-5, 10), 5)
        
    def test_sumar_argumentos_no_numericos(self):
        """Prueba que la función lanza un TypeError con entradas no numéricas."""
        with self.assertRaises(TypeError):
            sumar('a', 5)

if __name__ == '__main__':
    unittest.main()