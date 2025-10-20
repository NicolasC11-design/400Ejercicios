class Clase12:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 12: {self.dato}'
NicolasCristiano = Clase12('Ejemplo')
print(NicolasCristiano.mostrar())
