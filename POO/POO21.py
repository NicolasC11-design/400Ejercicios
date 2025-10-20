class Clase21:
    def __init__(self, dato):
        self.dato = dato
    def mostrar(self):
        return f'Clase 21: {self.dato}'
NicolasCristiano = Clase21('Ejemplo')
print(NicolasCristiano.mostrar())
