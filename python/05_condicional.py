#condicional if
#simple

combustible = 10
if combustible >= 20:
    print("puedes despegar")

#condicional if-else
creditos = int(input("Ingrese la cantidad de créditos que tienes: "))    
precio_repuesto = int(input("Ingrese el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("puedes comprar el repuesto")
else:
    print("no puedes comprar el repuesto")

#if anidado
if creditos >= precio_repuesto:
    print("puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("te sobran créditos")
    else:
        print("te quedas con los créditos necesarios") 
else:
    print("no tienes suficientes créditos para comprar el repuesto")

#condicional if-elif-else

if creditos >= precio_repuesto:
    print("puedes comprar el repuesto y te sobran créditos")
elif creditos == precio_repuesto:
    print("puedes comprar el repuesto y te quedas con los créditos necesarios")
else:
    print("no tienes suficientes créditos para comprar el repuesto")

tipo_repuesto = input("Ingrese el tipo de repuesto que desea comprar (motor,alas  o escudos ): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "alas":
    print("puedes comprar el repuesto y te sobran créditos")
elif tipo_repuesto == "alas" and creditos >= precio_repuesto:
    print("puedes comprar el repuesto y te quedas con los créditos necesarios")
elif tipo_repuesto == "escudos" and creditos >= precio_repuesto :
    print("puedes comprar el repuesto y te quedas con los créditos necesarios")
else:
    print("no puedes comprar el repuesto")  