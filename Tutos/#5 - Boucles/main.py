# importation du randint
from random import randint

# choisir un nombre aleatoire entre 1 et 1000
just_price = randint(1, 1000)

# statut du jeu (activé/désactivé)
running = True

# tant que le jeu est en cours d'éxécution
while running:
#entrer le numero
    number = int(input("Entrer un prix"))

    # si le nombre est exact
    if number == just_price:
        print("C'est gagne!")
        print("Fin du jeu")
        break  # casse le programme

    # si le nombre et superieur
    elif number > just_price:
        print("C'est moins!")

    # si le nombre est superieur
    elif number < just_price:
        print("C'est plus!")
