class Clase2:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 2: {self.dato}'
NicolasCristiano = Clase2('Ejemplo')
print(NicolasCristiano.mostrar())
