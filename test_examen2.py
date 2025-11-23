import unittest
from Examen2 import MiClase 

class TestMiClase(unittest.TestCase):

    def test_ObtieneValencia_caso1(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)  # los dígitos impares son 1, 3, 5, 7

    def test_ObtieneValencia_caso2(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.ObtieneValencia(24680)
        self.assertEqual(resultado, 0)  # no hay dígitos impares



    def test_DivisibleTempo_caso1(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])

    def test_DivisibleTempo_caso2(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7]) 

    def test_Encuentra_caso1(self):
        obj = MiClase(0,0,0,[],[])
        self.assertTrue(obj.Encuentra([1,2,3,4], 3))  
        
    def test_Encuentra_caso2(self):
        obj = MiClase(0,0,0,[],[])
        self.assertFalse(obj.Encuentra([1,2,3,4], 5))  
 

if __name__ == '__main__':
    unittest.main()