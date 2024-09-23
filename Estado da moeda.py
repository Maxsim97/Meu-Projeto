#Registrar o conteúdo e a sua nota...
CONTEUDO = input("Qual o filme ou série preferido?")
AVALIAÇÃO = (input("Atribuir uma nota de 1 à 5:"))

# Realizar a avaliação...
match AVALIAÇÃO:
    case 1:
        print("Péssimo")
        PORQUE = input("Descreva porque a avaliação foi baixa:")
    case 2:
        print("Ruim!")
        PORQUE = input("Descreva porque a avaliação foi baixa:")
    case 3:
        print("Razoável")
    case 4:
        print("Bom")
    case 5:
        print("Ótimo!")
    case _:
        print("Opção não reconhecida...")
