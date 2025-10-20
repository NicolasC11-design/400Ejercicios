class Clase7:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 7: {self.dato}'
NicolasCristiano = Clase7('Ejemplo')
print(NicolasCristiano.mostrar())
