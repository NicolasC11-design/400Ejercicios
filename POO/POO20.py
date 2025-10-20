class Clase20:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 20: {self.dato}'
NicolasCristiano = Clase20('Ejemplo')
print(NicolasCristiano.mostrar())
