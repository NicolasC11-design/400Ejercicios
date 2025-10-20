class Clase33:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 33: {self.dato}'
NicolasCristiano = Clase33('Ejemplo')
print(NicolasCristiano.mostrar())
