class Clase15:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 15: {self.dato}'
NicolasCristiano = Clase15('Ejemplo')
print(NicolasCristiano.mostrar())
