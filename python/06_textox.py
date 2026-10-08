# string cadena de caracteres

jedi = "Qui-Gon Jinn"
aprendiz = "Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("El jedi es:" + jedi)
print("El jedi", type(jedi))
print("El aprendiz es:" + aprendiz)
print("El aprendiz", type(aprendiz))
print("El droide es:" + droide)
print("El droide", type(droide))
print("El planeta es:" + planeta)
print("El planeta", type(planeta))
print("El codigo es:" + codigo)
print("El codigo", type(codigo))

longitud_jedi = len(jedi)
print("La longitud del nombre del jedi es:" + str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es:" + str(longitud_aprendiz))

mensaje = "la federacion de comercio ha establecido un bloqueo en el planeta Naboo"
print("El mensaje es:" + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayusculas es:" + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minusculas es:" + mensaje_minusculas)

comunicado = "los jedi son enviados a Naboo"
print("El comunicado es:" + comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("El nuevo comunicado es:" + nuevo_comunicado)

planetas = "Naboo, Tatooine, Coruscant, Alderaan"
planetas_lista = planetas.split(", ")
print("planetas_lista")
print("la lista de planetas es :" + str(planetas_lista))
print("el primer planeta es:" + planetas_lista[0])

droide = "R2-D2"
print("El droide es:" + droide)
print("El droide", type(droide))
print("el primer caracter del droide es:" + droide[0])
print("el segundo caracter del droide es:" + droide[1])
print("el tercer caracter del droide es:" + droide[2])
print("el cuarto caracter del droide es:" + droide[3])
print("el quinto caracter del droide es:" + droide[4])
print("el sexto caracter del droide es:" + droide[-1])


planeta =  "   Naboo     "
print("El planeta es:" + planeta)
print("El planeta sin espacios es:" + planeta.strip())
