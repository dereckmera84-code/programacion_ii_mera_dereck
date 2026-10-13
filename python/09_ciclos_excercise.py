
"""
Control de Flota de Naboo
"""

nave = [
    {
        "nombre": "Caza N-1",
        "combustible": 80,
        "droide": ["R2-D2", "R2-A6"]
    },
    {
        "nombre": "Caza Real",
        "combustible": 35,
        "droide": ["R2-N3"]
    },
    {
        "nombre": "Transporte",
        "combustible": 65,
        "droide": ["R2-D2", "R2-A6"]
    }
]

naves_listas = 0
naves_recarga = 0
total_droides = 0
total_ciclo = 0

for numero, naves in enumerate(nave, start=1):
    print(f"--- Nave: {numero} - {naves['nombre']}")

    if naves["combustible"] >= 50:
        print("Estado inicial: lista")
        naves_listas += 1
    else:
        print("Estado inicial: Recargar")
        naves_recarga += 1

        ciclo = 0
        while naves["combustible"] < 50:
            ciclo += 1
            naves["combustible"] += 10

        total_ciclo += ciclo
        print("Recarga completa")
        print("Estado final: LISTA")

    total_droides += len(naves["droide"])

    for droides in naves["droide"]:
        print(f"Droide: {droides}")

print("=========================================")
print("RESUMEN")
print("=========================================")
print(f"Total naves: {len(nave)}")
print(f"Naves listas inicialmente: {naves_listas}")
print(f"Naves recargadas: {naves_recarga}")
print(f"Total droides: {total_droides}")
print(f"Total ciclos: {total_ciclo}")
