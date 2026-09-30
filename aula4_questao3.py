while True:
    Ano = int(input("É bissexto? Digite um ano para descobir: "))

    if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
        print("Bissexto")
    else:
        print("Não Bissexto")