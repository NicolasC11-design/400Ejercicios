class Clase22:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 22: {self.dato}'
NicolasCristiano = Clase22('Ejemplo')
print(NicolasCristiano.mostrar())
