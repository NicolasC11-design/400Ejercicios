class Clase42:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 42: {self.dato}'
NicolasCristiano = Clase42('Ejemplo')
print(NicolasCristiano.mostrar())
