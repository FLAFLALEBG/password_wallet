# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Création variable "profile" et demande le mot de passe
    profile = input("Entrez le nom du profile : ")
    pswd = input("Veuillez entrer le mot de passe : ")
    pswd_lenght = len(pswd)
    print("Votre mot de passe fait " + str(pswd_lenght) + " caractères")
    if pswd_lenght < 6:
       pswd = input("Trop court : ")
       print("Hey, " + str(profile) + ", voici votre mot de passe : '" + str(pswd) + "' .")

main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
