class Clase8:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 8: {self.dato}'
NicolasCristiano = Clase8('Ejemplo')
print(NicolasCristiano.mostrar())
