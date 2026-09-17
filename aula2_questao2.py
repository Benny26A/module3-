age_juliana = int(input("Digite a idade de Juliana: "))
age_cris = int(input("Digite a idade de Cris: "))
responsável= int(input("Digite a idade do Responsável: "))
if age_juliana > 17 and age_cris > 17 or responsável > 17:
    print("True - Podem entrar no bar")
else:
    print("False - Não podem entrar no bar")