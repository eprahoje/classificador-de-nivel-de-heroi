heroName = input("Digite o nome do seu héroi: ")
xp = int(input("Digite o nível do seu héroi: "))


def levelClassificator():

    if xp <= 1000:
        level = "Ferro"
    elif xp >= 1001 and xp <= 2000:
        level = "Bronze"
    elif xp >= 2001 and xp <= 5000:
        level = "Prata"
    elif xp >= 5001 and xp <= 7000:
        level = "Ouro"
    elif xp >= 7001 and xp <= 8000:
        level = "Platina"
    elif xp >= 8001 and xp <= 9000:
        level = "Ascendente"
    elif xp >= 9001 and xp <= 10000:
        level = "Imortal"
    elif xp >= 10001:
        level = "Radiante"

    print(f"O Herói de nome {heroName} está no nível de {level}")

levelClassificator()
