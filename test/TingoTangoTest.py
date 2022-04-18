import unittest
from src.TingoTango import TingoTango

class TingoTangoPrueba(unittest.TestCase):
    def setUp(self):
        self.TT = TingoTango()

    def tearDown(self):
        self.TT = None

    def test_tingoTango_multiploTres_retornaTingo(self):
        #Arrange
        self.numero1 = 3
        self.numero2 = 6
        self.resultadoEsperado1 = 'Tingo'
        self.resultadoEsperado2 = 'Tingo'
        #Do
        self.resultadoActual1 = self.TT.textoTingoTango(self.numero1)
        self.resultadoActual2 = self.TT.textoTingoTango(self.numero2)
        #Assert
        self.assertEqual(self.resultadoEsperado1, self.resultadoActual1)
        self.assertEqual(self.resultadoEsperado2, self.resultadoActual2)


