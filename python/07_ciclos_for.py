#ciclos for

naves=[
    "Caza N-1",
    "Nave real de Naboo",
    "Transporte"
]
for nave in naves:
    print("Inspeccionando nave:", nave)

print("Inspeccion realizada")

rondas = range(1, 6)

print("Tipo de rondas:", type(rondas))
for ronda in rondas:
    print(f"Ronda de vigilancia {ronda}")
    print(f"Tipos de datos ronda: {type(ronda)}")

droides = range(1, 17, 3)

print("Tipo de droides:", type(droides))
for droides in droides:
    print(f"Reparar: droide B1 {droides}")
    print(f"Tipos de datos droid: {type(droides)}")


planetas = [
    "Naboo",
    "Tatooine",
    "Coruscant"
]      

recorrido = enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipo de dato {type(posicion)}: {type(planeta)}")

paises = [
    "Ecuador",
    "Venezuela",
    "CHile",
    "Colombia"
    "Brasil",
    "ESTADOS UNIDOS",
]
for pais in paises:
    if pais == "CHile":
        continue
    if pais == "Brasil":
        break
    print(f"Pais visitado: {pais}")

jedi = {}
jedi_activo = {
    "nombre": "Obiwan",
    "fuerza": "120",
    "estilo_pelea": "samurai",
    "misiones": ["gerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion":{
        "estarura":1.80,
        "especie": "humana"
    }
}
print(jedi_activo)
nave =dict(nombre = "AZ-1", capacidad = 8, turbo_laser = 2)
print(nave)

jedi["nombre"] = "Luck"
jedi["fuerza"] = 150 
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave} -{valor}")
