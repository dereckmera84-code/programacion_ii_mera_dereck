from abc import ABC, abstractmethod

class NaveEspacial(ABC):
    modelo: str

    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def despegar(self):
        pass


class NaveCapsula(NaveEspacial):
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "despega con motores de capsule corp")


class NaveSaiyajin(NaveEspacial):
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "despega inmediatamente")


nave_Bulma = NaveCapsula("Nave de Bulma")
nave_Vegeta = NaveSaiyajin("Capsula Saiyajin")
nave_Bulma.despegar()
nave_Vegeta.despegar()
