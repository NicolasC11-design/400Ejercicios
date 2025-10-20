class Clase5:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 5: {self.dato}'
NicolasCristiano = Clase5('Ejemplo')
print(NicolasCristiano.mostrar())
