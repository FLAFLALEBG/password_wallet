from tkinter import *

def password_generator():

    window = Tk()
    window.title("Génrateur de mot de passe")
    window.geometry("900x800")
    window.minsize(450, 600)
    window.config(background='#BFBFBF')

    label_title = Label(window, text="Bienvenue sur le générateur de mot de passe", font=("Arial", 20), bg='#BFBFBF')
    label_title.pack(side=TOP, expand=True)

    window.mainloop()