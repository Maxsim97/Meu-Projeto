#Criar programa para usuário...
print("Digite sua nota 1:")
NOTA1 = int(input())
print("Digite a nota 2:")
NOTA2 = int(input())
print("Digite a nota 3:")
NOTA3 = int(input())
print("Digite a nota 4:")
NOTA4 = int(input())

#Calcular média...
MEDIA = (NOTA1 + NOTA2 + NOTA3 + NOTA4)/4

if MEDIA >= 6:
    print("Aluno aprovado!")
elif MEDIA < 6:
    print("Aluno reprovado!")
    
print ("BOA SORTE!")

