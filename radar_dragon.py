class RadarDragon:
    region1: int
    region2: int

    def __init__(self, region1: int, region2: int):
        self.region1 = region1
        self.region2 = region2

    def buscar_esferas(self):
        encontradas = self.region1 + self.region2
        faltantes = 7 - encontradas
        return encontradas, faltantes

Radar_Bulma = RadarDragon(3, 2)
encontradas, faltantes = Radar_Bulma.buscar_esferas()

print("Esferas encontradas:", encontradas)
print("Esferas que faltan:", faltantes)    
