class Clase10:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 10: {self.dato}'
NicolasCristiano = Clase10('Ejemplo')
print(NicolasCristiano.mostrar())
