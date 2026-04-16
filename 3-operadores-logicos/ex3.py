print("Para continuar sua jornada")
print("Você deve obter a Benção dos mestres da guilda")
print("para isso você deve ter: ")
print("Sorte, ouro e a Chave secreta")

bless = 0
lucky = int(input("Quanto de sorte você tem? "))
gold = int(input("Quanto ouro você tem? "))
secret_key = input("Você possui a chave? ")

if gold >= 100 and secret_key == "sim":
    print("Você recebe duas aprovações")
    bless += 2
else:
    print("Precisa de mais ouro ou da chave")
    exit(0)

    if lucky < 2 or bless >= 2:
        print("Você consegue todas as aprovações")
    else: 
        print("Tente outro dia.")
        exit(0)