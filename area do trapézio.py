import os

base_maior = int( input("Dê um valor à base maior do trapézio: "))
base_menor = int( input("Dê um valor à base menor do trapézio: "))
altura = int( input("Dê um valor à altura do trapézio: "))

area = ((base_maior + base_menor) * altura) / 2

os.system('cls')

print("A area do trapézio é:", area)