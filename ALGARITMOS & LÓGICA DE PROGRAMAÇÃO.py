#Demonstração do uso de if/elif/else...
print("Digite a sua idade:")
IDADE = int(input())

if IDADE < 18:
    print("Você não é maior de idade!")
    print("Não podera realizar a operação!")
elif IDADE >= 65:
    print("Você já está pronto para se aposentar?")
    print("Podemos oferecer suporte técnico...")    
else:
    print("Você é maior de idade.")
    print("Portanto, poderá realizar a operação.")

print("Obrigado por optar pelos nossos serviços")

