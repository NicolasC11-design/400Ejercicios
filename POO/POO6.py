class Clase6:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 6: {self.dato}'
NicolasCristiano = Clase6('Ejemplo')
print(NicolasCristiano.mostrar())
