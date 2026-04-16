name = input("Seu nome? ")
classe = input("Classe? ")
hp = int(input("Vida inicial? "))
gold = int(input("Ouro inicial? "))

hero = {
    "nome": name,
    "classe": classe,
    "hp": hp,
    "ouro": gold
}

enemy = {
    "nome": "Goblin",
    "vida": 20,
    "ataque": 10,
    "ouro_derrotado": 20
}

print("\nNome", hero["nome"])
print("Classe", hero["classe"])
print("Vida", hero["hp"])
print("Ouro", hero["ouro"])

print("\nVocê entra na masmorra e encontra um barril")
choice = input("Deseja olhar o que tem dentro? ")
if choice == "sim":
    hero["poções"] = "poção de vida"
    print("Você achou uma poção de vida")
else:
    print("Você continua explorando")

print("\nMais a frente você encontra um inimigo")
print(f"um {enemy["nome"]} com {enemy["vida"]} de vida")

while enemy["vida"] > 0:
    combat = input("Atacar ou correr?")
    if combat == "atacar":
        print(f"Você ataca o {enemy["nome"]}")
        enemy["vida"] = enemy["vida"] - 10
        print(f"Agora ele tem {enemy["vida"]}")
    else:
        print("O goblin te mata")
        print("VOCÊ MORREU")
        break
