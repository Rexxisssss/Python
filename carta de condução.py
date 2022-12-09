import os

idade = int( input("Escreva a sua idade: "))

os.system('cls')

if idade < 18:
    
    print(f"Tens {idade} anos, não podes tirar a carta de condução.")
    
elif idade > 18:
    
    print(f"Tens {idade} anos, podes tirar a carta de condução.")