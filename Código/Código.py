import os
import turtle

MemFI = {1:0,2:1,3:1}

def Fibonachi_Mem(numero):
    if numero in MemFI:
        return MemFI[numero]
    MemFI[numero] = Fibonachi_Mem(numero-1)+Fibonachi_Mem(numero-2)
    return MemFI[numero]

def Fibonachi(objetivo):
    f1=0
    f2=1
    for i in range(1,objetivo-1):
        f1,f2 = f2,f1+f2
    return f2

def Fibonachi_RE(obj):
    if obj == 1:
        return 0
    if obj == 2 or obj == 3:
        return 1
    return Fibonachi_RE(obj-1)+Fibonachi_RE(obj-2)

def FactorialRE(num):
    if num < 2:
        return 1
    return num*FactorialRE(num-1)

def Factorial(num):
    fact=1
    for i in range(int(num),1,-1):
        fact *= i
    return fact

print("Factorial Recursivo\n\a")
n_calc = int(input("Ingresa un dato para calcular su factorial\n\t->"))
resultado = FactorialRE(n_calc)
Enter = input("el resultado es: "+str(resultado)+" PRESIONA ENTER PARA CONTINUAR")
os.system('cls')

print("Factorial Iterativo\n\a")
n_calc = int(input("Ingresa un dato para calcular su factorial\n\t->"))
resultado = Factorial(n_calc)
Enter = input("el resultado es: "+str(resultado)+" PRESIONA ENTER PARA CONTINUAR")
os.system('cls')

print("Fibonacci Iterativo\n\a")
Fibonacci = int(input("Ingresa el valor para calcular en la serie de Fibonacci\n\t->"))
Fibonacci = Fibonachi(Fibonacci)
print(Fibonacci)
Enter = input("PRESIONA ENTER PARA CONTINUAR")
os.system('cls')

print("Fibonacci Recursivo\n\a")
Fibonacci = int(input("Ingresa el valor para calcular en la serie de Fibonacci\n\t->"))
Fibonacci = Fibonachi_RE(Fibonacci)
print(Fibonacci)
Enter = input("PRESIONA ENTER PARA CONTINUAR")
os.system('cls')

print("Fibonacci con Memoria\n\a")
Fibonacci = int(input("Ingresa el valor para calcular en la serie de Fibonacci\n\t->"))
Fibonacci = Fibonachi_Mem(Fibonacci)
print(Fibonacci)
Enter = input("PRESIONA ENTER PARA CONTINUAR")
os.system('cls')
