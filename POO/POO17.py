class Clase17:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 17: {self.dato}'
NicolasCristiano = Clase17('Ejemplo')
print(NicolasCristiano.mostrar())
