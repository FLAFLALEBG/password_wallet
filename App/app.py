from tkinter import *
import webbrowser

def open_github_link():
    webbrowser.open_new_tab("https://github.com/FLAFLALEBG/password_wallet")

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
create_account_button = Button(window, text="Créer un Profile", font=("Arial", 20), bg='#BFBFBF')
create_account_button.pack(side=BOTTOM, expand=True, pady=40, fill=X)

# affichage
window.mainloop()