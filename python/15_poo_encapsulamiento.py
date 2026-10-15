class Guerrero:
    nombre:str
    poder: int

    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.poder = poder

    def get_poder(self):
        return self.poder

Vegeta = Guerrero("Vegeta", 8000)
print("Guerrero", Vegeta.nombre) 
print("Poder: ", Vegeta.get_poder())


class CuentaZeni:
    titular: str
    saldo: int

    def __init__(self, titular: str, saldo: int):
        self.titular = titular
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def retirar_dinero(self, cantidad: int):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro realizado", cantidad)
        else:
            print("Retiro no permitido")

cuenta = CuentaZeni("Mr. Satan", 5000)
print("titular:", cuenta.titular)
print("saldo inicial", cuenta.get_saldo())
cuenta.retirar_dinero(500)
print("salo final", cuenta.get_saldo())

