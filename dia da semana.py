#Solução do programa da semana...

print = input("Digite o dia da semana:")

match DIA:
    case "segunda":
        print("Vou para academia!")
    case "terça":
        print("Melhor não contar...")
    case "quarta":
        print("Vou à praia.")
    case "quinta"
        print("Vou ao cinema")
    case "sexta":
        print("Vou beber todas!")
    case "sábado":
        print("Vou descansar...")
    case "domingo":
        print("Vou à missa.")
    case _:
        print("Não entendi...")
        
