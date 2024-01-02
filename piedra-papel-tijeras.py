
import random

list=["piedra", "papel", "tijera" ]
respuesta = input("Escriba su selección: Piedra, Papel, o Tijera: ")
respuestaPC = random.choice(list)
respuesta=respuesta.lower()

print("Su apuesta es: ", respuesta)
print("La apuesta del PC es: ", respuestaPC)

def juego():
    if respuesta == respuestaPC:
        print("Tenemos un empate")
    elif (respuesta == "piedra" and respuestaPC == "tijera") or (respuesta == "papel" and respuestaPC == "piedra") or (respuesta == "tijera" and respuestaPC == "papel"):
        print("Has ganado")
    elif respuesta not in list:
        print("Esta respuesta no es válida")
    else:
        print("Has perdido")

juego()