class Clase1:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 1: {self.dato}'
NicolasCristiano = Clase1('Ejemplo')
print(NicolasCristiano.mostrar())
