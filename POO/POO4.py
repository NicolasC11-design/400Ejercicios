class Clase4:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 4: {self.dato}'
NicolasCristiano = Clase4('Ejemplo')
print(NicolasCristiano.mostrar())
