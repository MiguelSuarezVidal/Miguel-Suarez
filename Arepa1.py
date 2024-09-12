print("Introduzca la cantidad de ingredientes para hacer una arepa")
agua = float(input("Cuantas tazas de agua: "))
print("La cantidad de agua es: ",agua)
harina= float(input("Cuantas tazas de harina: ")) 
print("La cantidad de harina es",harina)
sal= (float(input("Cuantas cdas de sal: ")))/16/3
print("La cantidad de sal es",sal)
aceite= (float(input("Cuantas cdas de aceite: ")))/16
bol = agua + harina + sal
budare = bol + aceite
print("La arepa tiene un volumen de: ",budare)
input("Presione enter para continuar")