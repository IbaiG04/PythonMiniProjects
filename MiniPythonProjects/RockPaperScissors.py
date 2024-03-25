import random
a="piedra"
b="papel"
c="tijeras"

opciones = [a, b, c]
opcionPC=random.choice(opciones)

eleccion = input("Elige a.piedra || b.papel || c.tijeras: ")
if eleccion == "a" and opcionPC == c:
    print("ganaste")
    print("La PC eligio: ",opcionPC)
elif eleccion == "a" and opcionPC == b:
    print("perdiste")
    print("La PC eligio: ",opcionPC)
elif eleccion == "b" and opcionPC == a:
    print("ganaste")
    print("La PC eligio: ",opcionPC)
elif eleccion == "b" and opcionPC == c:
    print("perdiste")
    print("La PC eligio: ",opcionPC)
elif eleccion == "c" and opcionPC == b:
    print("ganaste")
    print("La PC eligio: ",opcionPC)
elif eleccion == "c" and opcionPC == a:
    print("perdiste")
    print("La PC eligio: ",opcionPC)
else:
    print("Empate")
    print("La PC eligio: ",opcionPC)

exec(open('RockPaperScissors.py').read())

