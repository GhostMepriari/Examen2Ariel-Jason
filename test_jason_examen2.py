import unittest
from Examen2 import MiClase


class TestMiClaseJason(unittest.TestCase):

    def setUp(self):
        self.objeto = MiClase(
            Valencia=5,
            Tempo=120,
            Tonos=12,
            listaCanciones=["Canción 1", "Canción 2", "Canción 3"],
            listaBailabilidad=[0.8, 0.9, 0.7]
        )

    # --------- ObtieneMasBailable ---------
    def test_obtiene_mas_bailable_lista_normal(self):
        resultado = self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.9)

    def test_obtiene_mas_bailable_valores_negativos(self):
        resultado = self.objeto.ObtieneMasBailable([-1.0, -0.5, -2.0])
        self.assertEqual(resultado, -0.5)

    # --------- VerificaListaCanciones ---------
    def test_verifica_lista_canciones_sin_none(self):
        resultado = self.objeto.VerificaListaCanciones(
            ["Canción 1", "Canción 2", "Canción 3"]
        )
        self.assertTrue(resultado)

    def test_verifica_lista_canciones_con_none(self):
        resultado = self.objeto.VerificaListaCanciones(
            ["Canción 1", None, "Canción 3"]
        )
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()
