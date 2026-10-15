class Guerrero:
    nombre: str
    poder: int
    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.poder = poder

    def saludar(self):
        print("Hola, soy:",self.nombre) 

    def entrenar(self):
        aumento = 200
        self.poder += aumento 

    def atacar(self, cantidad):
        daño = self.poder*cantidad
        print("Guerrero", self.nombre)
        print("Daño causado:", daño)

Goku = Guerrero("Goku", 9000)

Goku.saludar()

print("nombre del personaje:", Goku.nombre)
print("Poder del personaje", Goku.poder)
Goku.entrenar()
print("Poder del personaje: ", Goku.poder)
Goku.atacar(2)