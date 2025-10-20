class Clase100:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 100: {self.dato}'
NicolasCristiano = Clase100('Ejemplo')
print(NicolasCristiano.mostrar())
