# Tortuga_recursiva
import os
import argparse
import turtle

ap = argparse.ArgumentParser()
ap.add_argument("--huellas",required=True,help="Numero de Huellas")
args = vars(ap.parse_args())
huella = int(args["huellas"])

def Tortuga_recursiva(tortuga,espacio,huellas):
    if huellas>0:
        tortuga.stamp()
        espacio = espacio+3
        tortuga.forward(espacio)
        tortuga.right(24)
        Tortuga_recursiva(tortuga,espacio,huellas-1)

print("Camino de Tortuga Recursiva\n\a")
ven = turtle.Screen()
Donatello = turtle.Turtle()
Tortuga_recursiva(Donatello,1,huella)
ven.mainloop()
Enter = input("PRESIONA ENTER PARA CONTINUAR")
os.system('cls')
