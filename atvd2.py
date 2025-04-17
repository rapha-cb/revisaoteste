resp = "s"
while resp == "s":
    num = int(input("digite um numero: "))

    if num % 2 == 0:
        if num < 0:
            print(f"esse número {num} é par e é negativo")
        else:
            print(f"esse número {num} é par e positivo")
    else:
        if num < 0:
            print(f"esse número {num} é ímpar e negativo ")
        else:
            print(f"esse número {num} é ímpar e positivo")

    resp = input("deseja receber um novo número? (s/n)")