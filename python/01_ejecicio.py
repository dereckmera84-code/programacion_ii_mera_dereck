print("bienvenido a entregas")

America = 5.0
Europa = 7.5
Resto_del_mundo = 10.0

peso = float (input("Ingrese el peso del paquete en kg: "))
zona_destino = input("Ingrese la zona de destino (America, Europa o Resto del mundo): ")

if zona_destino == "America":
    precio_de_zona = America
elif zona_destino == "Europa":
    precio_de_zona = Europa
elif zona_destino == "Resto del mundo":
    precio_de_zona = Resto_del_mundo    
    print("El precio de la zona es:", precio_de_zona)
