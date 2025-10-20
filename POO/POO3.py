class Clase3:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 3: {self.dato}'
NicolasCristiano = Clase3('Ejemplo')
print(NicolasCristiano.mostrar())
