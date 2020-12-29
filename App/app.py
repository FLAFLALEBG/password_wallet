from tkinter import *
import webbrowser
from password_generator import password_generator


def open_github_link():
    webbrowser.open_new_tab("https://github.com/FLAFLALEBG/password_wallet")

def open_create_account_page():
    print()

# création fenetre principale
window = Tk()

# personalisation de la fenetre
window.title("Gestionnaire de mots de passe")
window.geometry("900x800")
window.minsize(450, 600)
window.maxsize(None, None)
window.config(background='#BFBFBF')

# ajout du texte et customisation de celui-ci
label_title = Label(window, text="Bienvenue sur votre gestionnaire de mot de passe", font=("Arial", 20), bg='#BFBFBF')
label_title.pack(side=TOP, expand=True)

# bouttons

open_github_link_button = Button(window, text="Découvrir le code source", font=("Arial", 10), bg='#BFBFBF', command=open_github_link)
open_github_link_button.pack(expand=TRUE, side=BOTTOM)

create_account_button = Button(window, text="Créer un Profile", font=("Arial", 20), bg='#BFBFBF', command=open_create_account_page)
create_account_button.pack(side=BOTTOM, expand=TRUE, fill=X)

password_generator_button = Button(window, text="Générateur de mots de passe", font=("Arial", 20), bg='#BFBFBF', command=password_generator)
password_generator_button.pack(side=BOTTOM, expand=True, fill=X)
# affichage
window.mainloop()
