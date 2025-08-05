
"""
Clase que representa un perro.
"""

class Perro:
    def __init__(self, nombre, raza):    
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("¡Guau, guau!")

    def presentarse(self):
        print("Mi nombre es: ",self.nombre," y soy un ", self.raza)

if __name__=="__main__":
    # Crear una instancia de la clase Perro
    perro1 = Perro("Fido", "Labrador")
    # Llamar a los métodos del objeto
    perro1.ladrar()
    perro1.presentarse()

    # Crear otra instancia de la clase Perro
    perro2 = Perro("Buddy", "Husky")
    perro2.presentarse()