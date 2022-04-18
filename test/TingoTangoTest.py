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
        self.numero2 = 5
        self.resultadoEsperado1 = 'Tingo'
        self.resultadoEsperado2 = 'Tango'
        #Do
        self.resultadoActual1 = self.TT.textoTingoTango(self.numero1)
        self.resultadoActual2 = self.TT.textoTingoTango(self.numero2)
        #Assert
        self.assertEqual(self.resultadoEsperado1, self.resultadoActual1)
        self.assertEqual(self.resultadoEsperado2, self.resultadoActual2)

    def test_tingoTango_multiploQuince_retornaTingoTango(self):
        #Arrange
        self.numero1 = 15
        self.resultadoEsperado1 = 'TingoTango'
        #Do
        self.resultadoActual1 = self.TT.textoTingoTango(self.numero1)
        #Assert
        self.assertEqual(self.resultadoEsperado1, self.resultadoActual1)

    def test_tingoTango_multiplo_retornaNumero(self):
        #Arrange
        self.numero1 = 7
        self.resultadoEsperado1 = '7'
        #Do
        self.resultadoActual1 = self.TT.textoTingoTango(self.numero1)
        #Assert
        self.assertEqual(self.resultadoEsperado1, self.resultadoActual1)

    def test_tingoTango_multiplo_retornaStr(self):
        #Arrange
        self.numero1 = '5'
        self.resultadoEsperado1 = 'Tango'
        #Do
        self.resultadoActual1 = self.TT.textoTingoTango(self.numero1)
        #Assert
        self.assertEqual(self.resultadoEsperado1, self.resultadoActual1)
