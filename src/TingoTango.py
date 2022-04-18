class TingoTango:
    def textoTingoTango(self, numero):
        if (not type(numero) is float) or (not type(numero) is int):
            try:
                numero = int(numero)
            except ValueError:
                print("ERRO: ingresa un entero")
                return None
        if (numero % 3 == 0) and (numero % 5 == 0):
            return 'TingoTango'
        if (numero % 3 == 0):
            return 'Tingo'
        if (numero % 5 == 0):
            return 'Tango'
        return str(numero)

#https://forms.gle/KyuDY2DhUoNJgivY7