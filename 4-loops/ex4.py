choice = input("Você está diante de um portal, deseja entrar? ")
if choice == "sim":
    for num in range(3, 0, -1):
        print(num)
    print("Você adentra o portal")
else:
    print("Você volta correndo para a Guilda")
    exit(0)