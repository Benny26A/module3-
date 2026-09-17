personagem = input("Escolha a classe (guerreiro, mago ou arqueiro): ")

forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

veracidade = (
    (personagem == "guerreiro" and forca >= 15 and magia <= 10)
    or
    (personagem == "mago" and forca <= 10 and magia >= 15)
    or
    (personagem == "arqueiro" and forca > 5 and forca <= 15 and magia > 5 and magia <= 15)
)

print("Pontos de atributo consistentes com a classe escolhida:", veracidade)