from poo_guerreros import Guerrero

class Saiyajin(Guerrero):
    def __int__(self, nombre:str):
        super().__int__(nombre)

    def transformarse(self):
        print(self.nombre, "Se transfoma en Super Saiyajin")

Goku = Saiyajin("Goku")
Goku.presentacion()
Goku.transformarse()

