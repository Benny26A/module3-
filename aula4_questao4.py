while True:

    dist= float(input("Por favor, informe a distância em Km: "))
    kilo= float(input("Por favor, informe a qtd de massa do pacote em kg: "))

    if dist <=100:
        price_for_kg=1.00

    if dist >=101 and dist <=300:
        price_for_kg=1.50 

    if dist >= 300:
        price_for_kg=2.00

    frete= kilo * price_for_kg

    if kilo > 10:
        frete += 10

    print(f"O valor total do frete é: R$ {frete:.2f}")