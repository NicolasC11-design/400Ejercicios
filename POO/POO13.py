class Clase13:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 13: {self.dato}'
NicolasCristiano = Clase13('Ejemplo')
print(NicolasCristiano.mostrar())
