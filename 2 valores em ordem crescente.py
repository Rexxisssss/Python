import os

num1 = int( input("Escreva um número inteiro: "))
num2 = int( input("Escreva outro número inteiro: "))

os.system('cls')

if num2 < num1:
    
    print(num2, "<", num1)

elif num2 > num1:

    print(num1, "<", num2)
