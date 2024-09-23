#Demostração de ooperações lógicos em condicionais...
print("O valor que você vai fazer amanhã de manhã?")
print("Dormir / estudar / planejar")
MANHA = input()
print("O que você vai fazer amanhã de tarde?")
print("Jogar / treinar / trabalhar")
TARDE = input()

if not MANHA or not TARDE:
    print("Você precisa dizer o que vai fazer!":)
    else:
        if MANHA == "dormir" or TARDE == "jogar":
            print("Você está desperdiçando seu dia!")
        elif MANHA == "estudar" or TARDE == "treinar:"
"