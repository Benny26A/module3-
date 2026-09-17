jogador = int(input("Digite sua idade: "))
qtd_jogos = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
won = int(input("Quantos jogos já venceu?: "))

membro= jogador >= 16 and jogador <=18 and qtd_jogos == True and won >=1

print("Apto para ingressar no clube de jogos de tabuleiro: ", membro)
