class Clase11:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 11: {self.dato}'
NicolasCristiano = Clase11('Ejemplo')
print(NicolasCristiano.mostrar())
