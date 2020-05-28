import os
import argparse
import turtle

print("Camino de Tortuga No Recursiva\n\a")
wind = turtle.Screen()
Rafael = turtle.Turtle()
size = 1
for i in range(30):
    Rafael.stamp()
    size=size+3
    Rafael.forward(size)
    Rafael.right(24)
wind.mainloop()
Enter = input("PRESIONA ENTER PARA CONTINUAR")
os.system('cls')
