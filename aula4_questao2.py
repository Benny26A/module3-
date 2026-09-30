while True:
    nota = int(input("Digite uma nota para esse filme (1 a 5): "))

    if nota == 5:
        print("Excelente!")
    elif nota == 4:
        print("Muito Bom!")
    elif nota == 3:
        print("Bom!")
    elif nota == 2:
        print("Regular!")
    elif nota == 1:
        print("Ruim!")
    else:
        print("Nota inválida! Por favor, digite um número de 1 a 5.\n")