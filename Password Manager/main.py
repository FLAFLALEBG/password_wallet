import os
import sys, traceback
import pwnedpasswords

# Variables :
profil = []


def main():
    print('''
\033[32m	  
________________________________________________________________________________________________________________________________________________________|/\|                                                                                                                                                                
8 888888888o            .8.             d888888o.      d888888o.   `8.`888b                 ,8'     ,o888888o.     8 888888888o.   8 888888888o.        |/\|                  
8 8888    `88.         .888.          .`8888:' `88.  .`8888:' `88.  `8.`888b               ,8'   . 8888     `88.   8 8888    `88.  8 8888    `^888.     |/\|                  
8 8888     `88        :88888.         8.`8888.   Y8  8.`8888.   Y8   `8.`888b             ,8'   ,8 8888       `8b  8 8888     `88  8 8888        `88.   |/\|                  
8 8888     ,88       . `88888.        `8.`8888.      `8.`8888.        `8.`888b     .b    ,8'    88 8888        `8b 8 8888     ,88  8 8888         `88   |/\|                  
8 8888.   ,88'      .8. `88888.        `8.`8888.      `8.`8888.        `8.`888b    88b  ,8'     88 8888         88 8 8888.   ,88'  8 8888          88   |/\|                  
8 888888888P'      .8`8. `88888.        `8.`8888.      `8.`8888.        `8.`888b .`888b,8'      88 8888         88 8 888888888P'   8 8888          88   |/\|                  
8 8888            .8' `8. `88888.        `8.`8888.      `8.`8888.        `8.`888b8.`8888'       88 8888        ,8P 8 8888`8b       8 8888         ,88   |/\|                  
8 8888           .8'   `8. `88888.   8b   `8.`8888. 8b   `8.`8888.        `8.`888`8.`88'        `8 8888       ,8P  8 8888 `8b.     8 8888        ,88'   |/\|                  
8 8888          .888888888. `88888.  `8b.  ;8.`8888 `8b.  ;8.`8888         `8.`8' `8,`'          ` 8888     ,88'   8 8888   `8b.   8 8888    ,o88P'     |/\|                  
8 8888         .8'       `8. `88888.  `Y8888P ,88P'  `Y8888P ,88P'          `8.`   `8'              `8888888P'     8 8888     `88. 8 888888888P'        |/\|                  \033[32m	
\033[31m
                                                                                                                                                        |/\|	
     ,o888888o.             .8.          8888888 8888888888 8 8888        8 8 8888888888   8 888888888o.    8 8888 b.             8      ,o888888o.     |/\|                  
    8888     `88.          .888.               8 8888       8 8888        8 8 8888         8 8888    `88.   8 8888 888o.          8     8888     `88.   |/\|                  
 ,8 8888       `8.        :88888.              8 8888       8 8888        8 8 8888         8 8888     `88   8 8888 Y88888o.       8  ,8 8888       `8.  |/\|                  
 88 8888                 . `88888.             8 8888       8 8888        8 8 8888         8 8888     ,88   8 8888 .`Y888888o.    8  88 8888            |/\|                  
 88 8888                .8. `88888.            8 8888       8 8888        8 8 888888888888 8 8888.   ,88'   8 8888 8o. `Y888888o. 8  88 8888            |/\|                  
 88 8888               .8`8. `88888.           8 8888       8 8888        8 8 8888         8 888888888P'    8 8888 8`Y8o. `Y88888o8  88 8888            |/\|                  
 88 8888   8888888    .8' `8. `88888.          8 8888       8 8888888888888 8 8888         8 8888`8b        8 8888 8   `Y8o. `Y8888  88 8888   8888888  |/\|                  
 `8 8888       .8'   .8'   `8. `88888.         8 8888       8 8888        8 8 8888         8 8888 `8b.      8 8888 8      `Y8o. `Y8  `8 8888       .8'  |/\|                  
    8888     ,88'   .888888888. `88888.        8 8888       8 8888        8 8 8888         8 8888   `8b.    8 8888 8         `Y8o.`     8888     ,88'   |/\|                  
     `8888888P'    .8'       `8. `88888.       8 8888       8 8888        8 8 888888888888 8 8888     `88.  8 8888 8            `Yo      `8888888P'     |/\|                  \033[31m
________________________________________________________________________________________________________________________________________________________|/\|
''')
    menu()


def menu():
    print("1) Créer un profile")
    print("2) Choisir un profile")
    print("3) Générer un mot de passe")
    print("4) Verifier un mot de passe")
    main_navigation = int(input("> "))

    if main_navigation == 1:
        create_profil()

    if main_navigation == 2:
        choose_profil()


def create_profil():
    # Création variable "profile" et demande le mot de passe
    new_profil = input("Nouveau profile : ")
    profil.append(new_profil)
    profile_len = len(profil)
    print("Parfait, profile crée. Retour au menu.")
    menu()


def choose_profil():
    print("Vous avez : ", len(profil), "profile(s)")
    if len(profil) >= 5:
        delete_profil()

    print("Voici vos profils : ")
    print("1)", profil[0])
    print("2)", profil[1])
    print("3)", profil[2])
    print("4)", profil[3])
    print("5)", profil[4]) 


def delete_profil():
    print("Vous avez plus de 5 profils veuillez en supprimer un.")
    print("Voici vos profils : ")
    print("1)", profil[0])
    print("2)", profil[1])
    print("3)", profil[2])
    print("4)", profil[3])
    print("5)", profil[4])
    del_profil_number = int(input("> "))
    del profil[del_profil_number]


if __name__ == "__main__":
    main()
