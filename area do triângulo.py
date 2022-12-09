import os

base = int( input("Dê um valor à base do triângulo: "))
altura = int( input("Dê um valor à altura do triângulo: "))

area = (base * altura)/2

os.system('cls')

print("A area do triângulo é ", area, "centimetros quadrados")