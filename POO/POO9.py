class Clase9:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 9: {self.dato}'
NicolasCristiano = Clase9('Ejemplo')
print(NicolasCristiano.mostrar())
