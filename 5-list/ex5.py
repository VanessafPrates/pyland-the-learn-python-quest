bag = ['Capa rasgada', 'Espada']

count = 0
while count < 4:
    choice = input("Quer adicionar um item ao sua bolsa? ")
    if choice == "sim":
        item1 = input("Qual item? ")
        bag.append(item1)
        print(f"Agora na sua bolsa tem {bag}")
    else:
        print("Até a proxima")
        break
    count += 1

for item in bag:
    print("Seus itens: ", item)

print("Primeiro item da bolsa: ", bag[0])