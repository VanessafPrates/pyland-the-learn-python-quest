level = 1

hp = int(input("Digite a vida do seu personagem: "))
key = input("Você tem a chave magica? ")

if hp < 30:
    print("Melhor você voltar e descansar")
elif key == "sim":
    print("A porta do castelo se abre.")
else:
    print("A porta continua fechada.")